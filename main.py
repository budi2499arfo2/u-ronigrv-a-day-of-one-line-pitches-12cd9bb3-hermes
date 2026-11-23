#!/usr/bin/env python3
"""A Day of One-Line Pitches.

Writes one original sentence to /output/entry.txt: a warm, direct pitch
to a friend who has never coded, whose app idea has waited three years —
describe it to an AI agent and let it build the first version before the
coffee goes cold.
"""

import os
import sys

TEXT = (
    "You've carried that app idea for years without a line "
    "of code — describe it to an AI agent on make.fun and let it "
    "build your first version before your coffee goes cold."
)


def main() -> int:
    # Gate: 1 to 240 characters, counted as Unicode code points,
    # and not only white space.
    if not (1 <= len(TEXT) <= 240) or not TEXT.strip():
        print("entry text fails the 1-240 gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and re-check: the file on disk must be exactly the text
    # we gated, byte for byte.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != TEXT or not (1 <= len(written) <= 240):
        print("written entry.txt does not match the gated text", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
