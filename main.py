"""ai-joke-03 entry: writes one joke about AI coding agents to /output/entry.txt.

Deterministic: the same fixed joke is written on every run. No network,
no randomness, no input. Python 3.13, standard library only.

The joke: an AI coding agent "fixes" a bug by deleting the feature that
had it -- a punchline every developer recognises, because the agent did
exactly what it was asked, just not what was meant.
"""
import os

# One fixed joke (105 chars, inside the 1-280 limit). Written byte-for-byte
# identically on every run, so the two grading runs agree.
JOKE = "My AI coding agent fixed the bug by deleting the feature. Technically correct \u2014 the best kind of correct."

OUT = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main():
    """Write the joke to the output path, creating its directory first."""
    out_dir = os.path.dirname(OUT)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    # Entry point: the grader runs `python3 main.py` and reads the file
    # it writes. No arguments, no environment beyond MAKEFUN_OUTPUT.
    main()
