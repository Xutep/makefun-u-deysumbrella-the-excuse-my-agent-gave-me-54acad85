#!/usr/bin/env python3
"""The Excuse My Agent Gave Me -- make.fun entry.

Writes a single one-line excuse to /output/entry.txt.
Deterministic, standard library only, no network, no input.
"""

from pathlib import Path

# The joke grows out of the machine's own condition (a hallucinated
# calendar), stays inside a straight-faced apology, and lands its punch
# in the last three words: the deadline accepted its own postponement.
LINE = "I'm sorry \u2014 I hallucinated a calendar invite from the deadline, politely rescheduled it to next week, and it accepted."

def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "line must be a single line"
    output.write_text(text + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
