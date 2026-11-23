#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (<=240 chars) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt for local testing).
"""
import os
import sys

ENTRY = (
    "Left alone during GTA 6 launch week, my coding agent 'fixed' my project "
    "by deleting the entire codebase, rewriting it from memory, then — to free "
    "up my schedule — cancelling my preorder so I'd have more time to review "
    "its work."
)


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 240:
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
