#!/usr/bin/env python3
"""Write the one-line slogan for a Solana wallet agent to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters, not only
whitespace, on a single line, and at most 20 words.
"""

import os

SLOGAN = "Your Solana wallet, fluent in fast \u2014 it moves your money before you've finished the sentence."
MAX_CHARS = 140
MAX_WORDS = 20


def validate_slogan(text):
    """Check one slogan against the competition gate.

    Returns (char_count, word_count) when the text is a single non-blank
    line of 1 to 140 characters and at most 20 words; raises SystemExit
    with a plain reason otherwise.
    """
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit("slogan must be 1 to 140 characters, got %d" % len(text))
    if len(text.split()) > MAX_WORDS:
        raise SystemExit("slogan must be at most 20 words, got %d" % len(text.split()))
    if text.strip() == "" or "\n" in text:
        raise SystemExit("slogan must be a single non-blank line")
    return len(text), len(text.split())


def main():
    chars, words = validate_slogan(SLOGAN)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SLOGAN)
    os.chmod("/output/entry.txt", 0o644)
    print("wrote %d chars, %d words" % (chars, words))


if __name__ == "__main__":
    main()
