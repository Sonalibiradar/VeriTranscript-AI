"""
All LLM calls go through this module. Every prompt enforces:
  - answer ONLY from the provided transcript segments (no outside knowledge)
  - explicit "not covered" if the transcript doesn't address the question
  - every claim backed by an exact quote + timestamp
  - strict JSON output so the app can parse + verify it programmatically

Swap providers by changing `call_llm()` — the rest of the app doesn't care
whether it's Claude, GPT, or a local model, as long as it returns text.
"""

import os
import json
import re
from typing import List, Dict

MODEL = os.environ.get("LLM_MODEL", "claude-sonnet-4-5")

_client = None


def _get_client():
    """Lazy import + lazy init: keeps this module importable (and unit-testable
    with a mocked call_llm) even if the `anthropic` package isn't installed yet."""
    global _client
    if _client is None:
        import anthropic  # imported here, not at module level, on purpose
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY not set. Copy .env.example to .env and add your key."
            )
        _client = anthropic.Anthropic(api_key=api_key)
    return _client


def call_llm(system: str, user: str, max_tokens: int = 1000) -> str:
    client = _get_client()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(block.text for block in resp.content if block.type == "text")


def _extract_json(raw: str) -> Dict:
    """Models occasionally wrap JSON in markdown fences or add stray text; strip that defensively."""
    cleaned = re.sub(r"^```(json)?|```$", "", raw.strip(), flags=re.MULTILINE).strip()
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        cleaned = match.group(0)
    return json.loads(cleaned)


# ---------------------------------------------------------------------------
# 1. Answer a single interview-guide question, for ONE transcript
# ---------------------------------------------------------------------------

ANSWER_SYSTEM = """You are analysing an expert-interview transcript for a market research project.
You must answer STRICTLY using the transcript excerpts provided below — never use outside knowledge,
never guess, and never invent a quote or timestamp.

Return ONLY valid JSON, no markdown fences, no commentary, in this exact shape:
{
  "covered": true or false,
  "answer": "a concise 1-3 sentence answer in your own words, or empty string if not covered",
  "quotes": [
    {"text": "exact verbatim quote copied from the excerpts", "timestamp": "MM:SS"}
  ]
}
Rules:
- "quotes" must be copied EXACTLY (verbatim, no paraphrasing) from the excerpts, including the timestamp attached to that excerpt.
- Include 1-2 of the strongest supporting quotes, not every sentence.
- If the excerpts do not address the question at all, set "covered": false, "answer": "", "quotes": [].
"""


def answer_question_for_transcript(question: str, segments) -> Dict:
    excerpt_block = "\n".join(f"[{s.timestamp}] {s.speaker}: {s.text}" for s in segments)
    user = f"""Interview guide question: "{question}"

Transcript excerpts:
{excerpt_block}

Respond with the JSON object only."""
    raw = call_llm(ANSWER_SYSTEM, user)
    try:
        return _extract_json(raw)
    except Exception:
        return {"covered": False, "answer": "", "quotes": [], "_raw_error": raw}


# ---------------------------------------------------------------------------
# 2. Cross-transcript theme & disagreement synthesis for ONE guide question
# ---------------------------------------------------------------------------

THEMES_SYSTEM = """You compare how three different experts answered the same interview question.
You are given each expert's answer (already grounded in their transcript) plus their supporting quotes.
Identify what they agree on and where they genuinely differ. Do not invent anything beyond what's given.

Return ONLY valid JSON, no markdown fences, in this exact shape:
{
  "common_themes": [
    {"theme": "short description", "supporting_experts": ["Expert A", "Expert B", "Expert C"]}
  ],
  "disagreements": [
    {"topic": "short description", "positions": [{"expert": "Expert A", "position": "short summary of their stance"}]}
  ]
}
If there is no real disagreement, return an empty "disagreements" list — do not manufacture one.
"""


def synthesize_themes(question: str, per_expert_answers: List[Dict]) -> Dict:
    block = "\n\n".join(
        f"{a['expert_name']} ({a['market']}): {a['answer']}\n"
        + "\n".join(f'  Quote [{q["timestamp"]}]: "{q["text"]}"' for q in a["quotes"])
        for a in per_expert_answers
        if a.get("covered")
    )
    if not block:
        return {"common_themes": [], "disagreements": []}

    user = f"""Interview guide question: "{question}"

Expert answers:
{block}

Respond with the JSON object only."""
    raw = call_llm(THEMES_SYSTEM, user, max_tokens=800)
    try:
        return _extract_json(raw)
    except Exception:
        return {"common_themes": [], "disagreements": [], "_raw_error": raw}


# ---------------------------------------------------------------------------
# 3. Free-form Q&A across all transcripts
# ---------------------------------------------------------------------------

CHAT_SYSTEM = """You answer a user's question using ONLY the transcript excerpts provided, which may
come from multiple experts across multiple markets. Never use outside knowledge. If the excerpts
don't contain enough to answer, say so explicitly rather than guessing.

Return ONLY valid JSON, no markdown fences, in this exact shape:
{
  "covered": true or false,
  "answer": "a clear answer synthesised across the relevant experts, in your own words",
  "quotes": [
    {"text": "exact verbatim quote", "timestamp": "MM:SS", "expert": "expert name"}
  ]
}
"""


def answer_freeform_question(question: str, segments_by_transcript: Dict[str, List]) -> Dict:
    blocks = []
    for tid, segs in segments_by_transcript.items():
        if not segs:
            continue
        expert = segs[0].expert_name
        market = segs[0].market
        lines = "\n".join(f"  [{s.timestamp}] {s.speaker}: {s.text}" for s in segs)
        blocks.append(f"{expert} ({market}):\n{lines}")
    excerpt_block = "\n\n".join(blocks)

    user = f"""User question: "{question}"

Transcript excerpts:
{excerpt_block}

Respond with the JSON object only."""
    raw = call_llm(CHAT_SYSTEM, user, max_tokens=900)
    try:
        return _extract_json(raw)
    except Exception:
        return {"covered": False, "answer": "", "quotes": [], "_raw_error": raw}
