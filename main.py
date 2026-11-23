"""Real-Life Patch Notes entry generator.

Writes one patch note, verbatim, to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

ENTRY = "v2.0.4: fixed a bug where the stomach growled loudest in rooms that had just gone silent."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The gate requires 1-160 chars of non-blank UTF-8 text.
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 chars"
    assert ENTRY.strip(), "entry must not be blank"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
