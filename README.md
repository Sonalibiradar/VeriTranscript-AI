# 🎙️ VeriTranscript AI (Hasamex Case Study)

> An AI-powered qualitative research platform that parses, retrieves, and synthesizes expert call transcripts with **100% ground-truth traceability and programmatic citation verification**.

> Zero-hallucination qualitative transcript analyzer. Answers interview-guide questions, identifies cross-market themes & disagreements, and programmatically verifies every quote against source audio timestamps.

### ⚡ Highlights:

- **Zero Hallucinations:** Prompts strictly forbid outside knowledge; unaddressed topics return "not covered".
- 
- **Programmatic Quote Verification:** Every quote and timestamp is verified via normalized substring matching against source text (`core/verify.py`).
- 
- **Cross-Market Synthesis:** Detects consensus themes and genuine divergences across European healthcare markets (France, Germany, UK).
- 
- **Deterministic Retrieval:** Fast, explainable TF-IDF + cosine similarity indexing expert responses only.
- 
- **Offline / Demo Mode Ready:** Works instantly out-of-the-box even without an active API key.
