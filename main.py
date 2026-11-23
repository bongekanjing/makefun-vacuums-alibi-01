#!/usr/bin/env python3
# The Vacuum's Alibi (102 chars, pure stdlib): writes the line to /output/entry.txt.
import os

LINE = "My sensors logged the spot as clean, the floor disagreed, and my battery has filed a formal complaint."

def main():
    os.makedirs("/output", exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200
    assert text.count(".") == 1 and text.endswith(".")
    assert "?" not in text and "!" not in text
    assert ". " not in text
    assert "\n" not in text and "\t" not in text
    assert text == text.strip()
    assert "  " not in text
    assert all(ch.isprintable() for ch in text)
    assert text[0].isupper()
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back: the file on disk must be byte-identical to the validated line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == text

if __name__ == "__main__":
    main()
