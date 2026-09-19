"""
Parses the expert-call transcript .txt files into structured segments.

Expected format (matches the provided case-pack files):

    Expert 1 – Dr. Jean Martin
    Role: Head of Urology
    Market: France

    00:00
    Interviewer: Thanks for joining...

    00:18
    Dr. Martin: Adoption is growing...

Each block is: a timestamp line (MM:SS) followed by "Speaker: text".
Blocks are separated by a blank line.
"""

import re
import os
from dataclasses import dataclass, asdict
from typing import List


TIMESTAMP_RE = re.compile(r"^(\d{1,2}:\d{2})$")
SPEAKER_LINE_RE = re.compile(r"^([^:]+):\s*(.+)$", re.DOTALL)


@dataclass
class Segment:
    transcript_id: str      # e.g. "Transcript_1_France"
    expert_name: str        # e.g. "Dr. Jean Martin"
    market: str              # e.g. "France"
    speaker: str             # e.g. "Dr. Martin" or "Interviewer"
    timestamp: str           # e.g. "01:20"
    text: str

    def as_dict(self):
        return asdict(self)


def _parse_header(header_block: str):
    """Pulls expert name / role / market out of the first block of the file."""
    lines = [l.strip() for l in header_block.strip().splitlines() if l.strip()]
    expert_name, market = "Unknown Expert", "Unknown Market"
    for line in lines:
        if line.lower().startswith("expert"):
            # "Expert 1 – Dr. Jean Martin" -> take text after the dash
            parts = re.split(r"[–-]", line, maxsplit=1)
            if len(parts) == 2:
                expert_name = parts[1].strip()
        elif line.lower().startswith("market:"):
            market = line.split(":", 1)[1].strip()
    return expert_name, market


def parse_transcript(file_path: str) -> List[Segment]:
    transcript_id = os.path.splitext(os.path.basename(file_path))[0]

    with open(file_path, "r", encoding="utf-8") as f:
        raw = f.read()

    # Blocks are separated by one or more blank lines
    blocks = [b for b in re.split(r"\n\s*\n", raw.strip()) if b.strip()]

    if not blocks:
        return []

    expert_name, market = _parse_header(blocks[0])

    segments: List[Segment] = []
    for block in blocks[1:]:
        lines = [l for l in block.splitlines() if l.strip() != ""]
        if not lines:
            continue

        ts_match = TIMESTAMP_RE.match(lines[0].strip())
        if not ts_match:
            # Not a well-formed timestamp block; skip defensively rather than crash
            continue
        timestamp = ts_match.group(1)

        remainder = " ".join(lines[1:]).strip()
        speaker_match = SPEAKER_LINE_RE.match(remainder)
        if speaker_match:
            speaker, text = speaker_match.group(1).strip(), speaker_match.group(2).strip()
        else:
            speaker, text = "Unknown", remainder

        segments.append(
            Segment(
                transcript_id=transcript_id,
                expert_name=expert_name,
                market=market,
                speaker=speaker,
                timestamp=timestamp,
                text=text,
            )
        )

    return segments


def parse_all(data_dir: str) -> List[Segment]:
    all_segments: List[Segment] = []
    for fname in sorted(os.listdir(data_dir)):
        if fname.lower().startswith("transcript") and fname.lower().endswith(".txt"):
            all_segments.extend(parse_transcript(os.path.join(data_dir, fname)))
    return all_segments


def load_interview_guide(file_path: str) -> List[str]:
    """Extracts the numbered questions from Interview_Guide.txt"""
    with open(file_path, "r", encoding="utf-8") as f:
        raw = f.read()
    questions = []
    for line in raw.splitlines():
        m = re.match(r"^\s*\d+\.\s*(.+)$", line.strip())
        if m:
            questions.append(m.group(1).strip())
    return questions


if __name__ == "__main__":
    # quick manual sanity check
    segs = parse_all(os.path.join(os.path.dirname(__file__), "..", "data"))
    for s in segs[:5]:
        print(s)
    print(f"\nTotal segments parsed: {len(segs)}")
    qs = load_interview_guide(os.path.join(os.path.dirname(__file__), "..", "data", "Interview_Guide.txt"))
    print(f"\nGuide questions: {qs}")
