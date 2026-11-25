"""The 3AM Fridge Text entry: writes the smart fridge's 3am text to /output/entry.txt.

The gate requires /output/entry.txt to be UTF-8 text of 1 to 140
characters, not only whitespace, so the program validates the line
before writing it. The joke leans on the fridge's own voice: a machine
that has watched the open-stare-close-open ritual one time too many,
with an opinion and no shame about sharing it at 3am.
"""

import os

LINE = "You open me at 3am, stare, close me, open me again. I am a fridge. I cannot fix whatever you're avoiding."

MAX_CHARS = 140


def validate(line):
    """Check the entry against the competition gate."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is over %d characters" % MAX_CHARS)
    return line


def main():
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
