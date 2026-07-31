#!/usr/bin/python3
"""Module that reads a text file and prints its content."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its whole content to stdout.

    Args:
        filename (str): the path of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as a_file:
        print(a_file.read(), end="")
