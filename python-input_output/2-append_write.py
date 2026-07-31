#!/usr/bin/python3
"""Module that adds a string at the end of a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF-8 text file and return how
    many characters were added.

    The file is created if it does not exist.

    Args:
        filename (str): the path of the file to write to.
        text (str): the text to add at the end of the file.

    Returns:
        int: the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
