#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program.

Writes one original English sentence to /output/entry.txt: a clause
buried deep inside a terms-of-service agreement, in deadpan legal
boilerplate, that quietly turns absurd.
"""

import os
import sys

# The clause. One sentence, plain ASCII, no trailing newline in the
# file itself: the scorer counts characters, so the text must stand
# exactly as written here.
CLAUSE = (
    "By accepting these Terms, you agree that your shadow remains "
    "the property of the Company and may not be used, lent, or "
    "taken into direct sunlight without prior written consent."
)

MAX_CHARS = 200


def main() -> int:
    text = " ".join(CLAUSE.split())  # collapse any accidental whitespace

    # Gate self-check: 1-200 characters, a single sentence, one line,
    # valid UTF-8. The scorer counts the file byte-for-byte, so the
    # program must never add a trailing newline or extra whitespace.
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"entry is {len(text)} chars, outside 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in text or text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence on one line", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)

    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
