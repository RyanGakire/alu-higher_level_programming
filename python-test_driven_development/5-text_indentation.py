#!/usr/bin/python3
"""Text indentation module.

This module holds a single function, ``text_indentation``, that prints
a text with two new lines after each of the characters ``.``, ``?``
and ``:``.
"""


def text_indentation(text):
    """Print ``text`` with two new lines after each ``.``, ``?`` and ``:``.

    Lines are printed without any space at their beginning or end.

    Args:
        text: The text to print, a string.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for character in text:
        line += character
        if character in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip() != "":
        print(line.strip(), end="")
