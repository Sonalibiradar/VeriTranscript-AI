# Expert Call Transcript Analyser — Hasamex AI Engineer Case Study

A small Streamlit app that analyses the 3 provided expert-call transcripts
(robotic surgery adoption — France / Germany / UK) and:

1. Answers each interview-guide question, per expert
2. Extracts exact supporting quotes for every answer
3. Shows the source timestamp for every quote
4. Identifies common themes and disagreements across the 3 experts
5. Lets you ask free-form questions across all transcripts

Every answer is grounded in the transcripts only — the app never lets the
model rely on outside knowledge, and every quote is **programmatically
verified** against the source text before being shown.

## Quickstart

```bash
git clone <this-repo>
cd hasamex_case
python -m venv venv && source venv/bin/activate   # optional but recommended
pip install -r requirements.txt

cp .env.example .env
# edit .env and add your ANTHROPIC_API_KEY

streamlit run app.py
```

Opens at `http://localhost:8501`. The 3 transcripts + interview guide are
already bundled in `data/` — no upload step needed for this demo, though
the parser (`core/parser.py`) works on any file dropped into that folder
following the same `MM:SS` / `Speaker: text` format.

## Architecture

```
data/*.txt
    │
    ▼
core/parser.py        → regex-based parse into Segment(transcript_id, expert_name,
                          market, speaker, timestamp, text)
    │
    ▼
core/retrieval.py      → TF-IDF + cosine similarity over expert segments
                          (interviewer lines excluded from the index)
    │
    ▼
core/llm.py             → 3 grounded prompts, all forced into strict JSON:
                            1. answer_question_for_transcript  (per expert, per guide question)
                            2. synthesize_themes                (cross-expert, per guide question)
                            3. answer_freeform_question          (cross-expert, ad-hoc question)
    │
    ▼
core/verify.py          → every quote the model returns is checked as a
                          normalized substring match against the actual
                          transcript text before being displayed
    │
    ▼
app.py (Streamlit)      → 3 tabs: Interview Guide / Themes & Disagreements / Ask a Question
```

## Key design decisions

**Retrieval: TF-IDF, not embeddings — at this scale.**
With ~40 segments across 3 transcripts, semantic embeddings are unnecessary
overhead. TF-IDF is deterministic, needs no model download, and is easy to
explain and debug live. See "Scaling to 30+ transcripts" below for how this
changes.

**Every quote is verified, not trusted.**
The LLM is asked to copy quotes verbatim, but LLMs still occasionally
paraphrase or misattribute. `core/verify.py` re-checks every returned quote
against the actual transcript text (normalized: lowercase, punctuation
stripped) and marks it ✅ verified or ⚠️ not found. This is the single most
important design decision for a task where "do not invent information" is
explicit in the brief — it turns "trust the model" into "verify the model."

**Retrieval before generation, not "dump the whole transcript."**
Even though these transcripts are short enough to fit in one prompt, the
app retrieves top-k relevant segments per question rather than sending the
full transcript. This is deliberate: it's the pattern that actually scales,
it keeps the LLM's context tightly scoped (reducing hallucination surface
area), and it's the same architecture you'd use with 30+ transcripts.

**Interviewer lines are excluded from the retrieval index.**
Only expert answers are indexed and quotable — the interviewer's questions
provide structure but shouldn't be returned as "supporting quotes."

**Strict JSON output + defensive parsing.**
Every prompt forces a JSON schema (`covered`, `answer`, `quotes`) so the
app can programmatically verify and render results rather than parsing
free text. `_extract_json()` defensively strips markdown fences in case the
model adds them anyway.

**"Not covered" is a first-class outcome.**
If a transcript doesn't address a guide question, the model is explicitly
instructed to say so (`covered: false`) rather than stretch an answer from
unrelated segments. This shows up in the UI as "not addressed in this
transcript" instead of a low-quality forced answer.

## Model choice

Claude (`claude-sonnet-4-5` by default, configurable via `LLM_MODEL` in
`.env`) for generation. The LLM call is isolated in `core/llm.py` behind a
single `call_llm()` function — swapping to GPT-4/GPT-5 or another provider
only requires changing that one function; nothing else in the app depends
on the provider.

## How hallucinations are reduced (summary)

1. Prompts restrict the model to the retrieved excerpts only, with explicit
   instructions never to use outside knowledge.
2. The model must say "not covered" rather than force an answer.
3. Every quote is required to be a verbatim copy — and is then independently
   checked against the source transcript text (`core/verify.py`), so a
   fabricated or misquoted "citation" is caught and flagged in the UI
   instead of silently trusted.
4. Retrieval scopes the model's context to only the most relevant segments,
   shrinking the space in which it could hallucinate.

## Scaling from 3 transcripts to 30+

- **Retrieval**: swap TF-IDF for real embeddings (e.g. `sentence-transformers`
  locally, or an embeddings API) and a vector store (Chroma/FAISS/pgvector)
  so retrieval quality holds up as segment count grows into the thousands.
- **Indexing pipeline**: move parsing/embedding into an offline batch job
  that runs once per new transcript upload, rather than re-parsing on every
  app load.
- **Theme synthesis at scale**: with 3 experts you can pass all per-expert
  answers into one synthesis call. With 30+, you'd cluster similar answers
  first (embedding similarity or a cheap classification pass), then run
  synthesis per cluster to keep the prompt size sane and the output
  structured.
- **Cost/latency**: batch guide-question answering across transcripts in
  parallel async calls instead of sequential loops; cache per-transcript,
  per-question answers so re-running the guide doesn't re-call the LLM for
  unchanged transcripts.
- **UI**: move from "load everything on start" to per-project transcript
  upload + a persisted store (so it's a real multi-project tool, not a
  fixed demo).

## Known limitations (given the time available)

- Retrieval is TF-IDF, so purely paraphrased content with no shared
  vocabulary between the question and the answer could be under-retrieved
  (embeddings would help here — see "Scaling" above).
- Theme synthesis re-runs per guide question; a smarter version would also
  look for themes that cut *across* different guide questions.
- No persistence/database — designed for a fixed 3-transcript demo, not
  production multi-user use.
