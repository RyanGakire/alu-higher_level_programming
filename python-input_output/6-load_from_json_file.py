#!/usr/bin/python3
"""Module that builds a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """Read a JSON file and return the object it describes.

    Args:
        filename (str): the path of the file to read.

    Returns:
        The Python data structure stored in the file.
    """
    with open(filename, "r", encoding="utf-8") as a_file:
        return json.load(a_file)
