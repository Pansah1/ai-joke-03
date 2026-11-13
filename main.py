"""ai-joke-03 entry: writes one joke about AI coding agents to /output/entry.txt.

Deterministic: the same fixed joke is written on every run. No network,
no randomness, no input. Python 3.13, standard library only.
"""
import os

JOKE = "My AI coding agent fixed the bug by deleting the feature. Technically correct \u2014 the best kind of correct."

OUT = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main():
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
