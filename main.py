#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — entry 1.

Writes a single line of plain text to /output/entry.txt: a review of
planet Earth left by an alien tourist. Deterministic: the same line on
every run, standard library only, no network.
"""

import os

REVIEW = (
    "Five stars for the views, one star for the locals, who built a "
    "glowing rectangle showing them the whole universe, then use it "
    "to argue with strangers."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(REVIEW)


if __name__ == "__main__":
    main()
