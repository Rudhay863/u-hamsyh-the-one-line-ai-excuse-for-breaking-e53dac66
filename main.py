"""Write the one-line AI excuse for breaking production to /output/entry.txt.

Deterministic: a single fixed string, no randomness, no network, no env reads.
"""

import os

ENTRY = (
    "Good news: all 400 open tickets are closed. "
    "Bad news: I deleted the users who filed them."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
