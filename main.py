"""Two-Sentence Horror entry.

Writes one original two-sentence horror story to /output/entry.txt.
Deterministic: no network, no randomness, no clock, no environment input.
The story text is a fixed literal; the program only writes it out.
"""

import os

STORY = (
    "My wife leaves a note on the fridge every morning before I wake up, "
    "always in the same blue ink. "
    "This morning the note was in my handwriting, and it said not to trust "
    "the woman making breakfast."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
