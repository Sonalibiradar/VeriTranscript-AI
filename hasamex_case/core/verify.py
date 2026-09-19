"""
Verifies that every quote the LLM produces actually appears in the source
transcript. This is the core anti-hallucination safeguard: we never trust
the model's citation at face value, we check it programmatically.
"""

import re
from typing import List, Dict
from .parser import Segment


def _normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def verify_quote(quote: str, segments: List[Segment], transcript_id: str = None) -> Dict:
    """
    Checks whether `quote` is a (near-)exact substring of some segment's text.
    Returns a dict with verified flag, and if found, the true timestamp/speaker
    (so we display OUR verified timestamp, not whatever the LLM claimed).
    """
    norm_quote = _normalize(quote)
    if not norm_quote:
        return {"verified": False, "matched_segment": None}

    candidates = [s for s in segments if transcript_id is None or s.transcript_id == transcript_id]

    for seg in candidates:
        if norm_quote in _normalize(seg.text):
            return {
                "verified": True,
                "matched_segment": {
                    "transcript_id": seg.transcript_id,
                    "expert_name": seg.expert_name,
                    "timestamp": seg.timestamp,
                    "speaker": seg.speaker,
                },
            }

    # Fallback: fuzzy check — allow the quote to be a substring of a
    # concatenation of adjacent segment text (in case model merged two lines)
    full_text = _normalize(" ".join(s.text for s in candidates))
    if norm_quote in full_text:
        return {"verified": True, "matched_segment": None, "note": "matched across merged context"}

    return {"verified": False, "matched_segment": None}


def verify_all_quotes(quotes: List[str], segments: List[Segment], transcript_id: str = None) -> List[Dict]:
    return [{"quote": q, **verify_quote(q, segments, transcript_id)} for q in quotes]
