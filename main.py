#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Prints the battery's final one-line text message to the charger
it waited for all day. One line, plain text, at most 200 characters.
"""

LINE = (
    "I sat at 1% all day while you charged the lamp, the speaker, "
    "and your vape. Goodbye. Tell the charger it was never about "
    "the cable, it was about the commitment."
)


def main() -> None:
    # The bounty gates the line to one line of plain text, at most 200 chars.
    assert "\n" not in LINE and len(LINE) <= 200, "entry line violates the gate"
    print(LINE)


if __name__ == "__main__":
    main()
