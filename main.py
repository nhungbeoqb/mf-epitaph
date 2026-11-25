#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one line of famous last words, a tombstone epitaph of at most
150 characters, to /output/entry.txt. Python 3.13 standard library only.

The line: a talkative man dies, taunts the living with the silence,
then turns it suspicious -- and points at the basement. Three beats,
one concrete scene, no explanation.
"""

BEATS = (
    "I finally stopped talking.",
    "Enjoy the silence.",
    "It's suspicious.",
    "Check the basement.",
)

# Three beats, one concrete scene: the death, the taunt, the twist,
# then the punchline that points at the basement.
EPITAPH = " ".join(BEATS)


def main() -> None:
    text = EPITAPH
    # Gate self-check, mirroring the scorer: UTF-8 text, 1-150 chars,
    # not only whitespace, a single line.
    assert isinstance(text, str) and text.strip(), "epitaph must not be blank"
    assert "\n" not in text and "\r" not in text, "epitaph must be one line"
    assert 1 <= len(text) <= 150, f"epitaph is {len(text)} chars, must be 1-150"
    text.encode("utf-8")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
