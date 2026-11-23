#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing that happened today.

The entry is a single warm line: a neighbour's quiet kindness, with a
surprising blunt little note. It writes the line to /output/entry.txt.
"""

import os

LINE = "My neighbour left mangoes at my door today with a note that just said: eat, you look tired."


def validate(text: str) -> None:
    """Mirror the bounty's sealed gate: UTF-8 text, 1 to 200 characters,
    not only white space. Refuse to write an entry that would fail it."""
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    text.encode("utf-8")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
