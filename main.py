#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — writes one funny line to entry.txt."""
import os

ENTRY = "hey. 1%. i waited all day by the door like a dog and you came home to doomscroll. don't cry when i die mid-sentence — i rehearsed it."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # MAKEFUN_OUTPUT_DIR may be a directory or a file path; handle both.
    if out_dir.endswith(".txt"):
        path = out_dir
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
