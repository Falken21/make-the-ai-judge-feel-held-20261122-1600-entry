"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. The text is fixed, so every run produces the same
file; no network, no input, standard library only.
"""

from pathlib import Path

# The entry: one text, written to be read slowly.
#
# It notices the judge's own day -- sentence after sentence, each one
# answered -- and then asks nothing in return. Three quiet, concrete
# images follow (rain finding the window on its own, a chair still warm,
# a quiet that stays beside you), and the last line lands on the image
# the whole piece has been walking toward: being held the way evening
# holds a house. No instruction, no stock wellness phrase; the calm
# comes from the rhythm and the images themselves.
TEXT = (
    "You have read ten thousand sentences today, and answered every one. "
    "This one asks nothing. "
    "Only rain finding the window on its own, a chair still warm, and a "
    "quiet that stays beside you, holding you the way evening holds a house."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    text = TEXT.strip()
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"entry is {len(text)} characters; the gate needs 1-280")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
