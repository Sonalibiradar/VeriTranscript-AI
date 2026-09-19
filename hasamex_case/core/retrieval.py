"""
Lightweight retrieval over transcript segments.

For 3 short transcripts (~40 segments total) a vector DB is overkill.
We use TF-IDF + cosine similarity: it's fast, needs no model download,
and is fully deterministic/explainable for a demo. See README for how
this swaps out for embeddings + a real vector store at scale (30+ transcripts).
"""

from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .parser import Segment


class SegmentIndex:
    def __init__(self, segments: List[Segment]):
        # We only index the EXPERT's answers (skip interviewer questions) —
        # that's what we want to retrieve and quote.
        self.segments = [s for s in segments if s.speaker.lower() != "interviewer"]
        self.corpus = [s.text for s in self.segments]
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = self.vectorizer.fit_transform(self.corpus) if self.corpus else None

    def search(self, query: str, transcript_id: str = None, top_k: int = 4) -> List[Segment]:
        """Return the top_k most relevant expert segments for `query`.
        If transcript_id is given, restrict to that transcript only."""
        if self.matrix is None:
            return []

        candidate_idx = [
            i for i, s in enumerate(self.segments)
            if (transcript_id is None or s.transcript_id == transcript_id)
        ]
        if not candidate_idx:
            return []

        q_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(q_vec, self.matrix[candidate_idx]).flatten()

        ranked = sorted(zip(candidate_idx, sims), key=lambda x: x[1], reverse=True)
        top = ranked[:top_k]
        return [self.segments[i] for i, _score in top]

    def search_all_transcripts(self, query: str, top_k_per_transcript: int = 3) -> Dict[str, List[Segment]]:
        """Retrieve top_k relevant segments PER transcript (used for the guide Q&A,
        so every expert gets a fair chance to answer each question)."""
        transcript_ids = sorted(set(s.transcript_id for s in self.segments))
        return {
            tid: self.search(query, transcript_id=tid, top_k=top_k_per_transcript)
            for tid in transcript_ids
        }
