#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete story told in exactly six words to /output/entry.txt.

The story: a lifetime of waiting, and the turn — after fifty years,
he is at the door. "Knocked" shows the moment of return instead of
telling it; why he left, why now, and whether she opens the door are
left for the reader to fill in.

Deterministic, standard library only, no network, no secrets.
"""

from pathlib import Path

# The story: exactly six words, 33 characters.
STORY = "She waited fifty years. He knocked."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(STORY, encoding="utf-8")
    words = STORY.split()
    print(f"Wrote {len(words)} words, {len(STORY)} characters to {OUTPUT_PATH}")
    print(STORY)


if __name__ == "__main__":
    main()
