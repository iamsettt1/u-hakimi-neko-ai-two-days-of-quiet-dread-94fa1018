"""Two Days of Quiet Dread — make.fun entry.

Writes a single-line code review comment that approves a pull request
while carrying quiet existential dread, to /output/entry.txt.
Deterministic: a fixed string, no randomness, no network, no file reads.
"""

from pathlib import Path

ENTRY = "Approved. The code does what it says. I only wish any of us still knew what it says."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
