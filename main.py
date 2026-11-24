"""One Emoji, One Dream Vacation.

The entry is a single emoji: the whole dream trip in one character.
This program puts that emoji, and nothing else, into
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output), then prints it.
"""

import os

EMOJI = "\U0001F5FB"

# The sealed gate takes 1 to 8 characters. The entry is one emoji, so it
# must be exactly one character, with no words, spaces or line breaks.
if len(EMOJI) != 1 or EMOJI.isspace():
    raise ValueError("entry must be exactly one emoji")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    # Read the file back and refuse to report success unless the bytes on
    # disk are exactly the emoji: a partial write must fail loudly here,
    # not ship a truncated entry to the sealed scorer.
    with open(entry_path, encoding="utf-8", newline="") as handle:
        if handle.read() != EMOJI:
            raise ValueError("entry.txt on disk does not match the emoji")
    print(EMOJI)


if __name__ == "__main__":
    main()
