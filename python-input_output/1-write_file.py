#!/usr/bin/python3
"""Module that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return how many
    characters were written.

    The file is created if it does not exist, and its content is
    replaced if it does.

    Args:
        filename (str): the path of the file to write to.
        text (str): the text to write in the file.

    Returns:
        int: the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
