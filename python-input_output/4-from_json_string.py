#!/usr/bin/python3
"""Module that turns a JSON string back into a Python object."""
import json


def from_json_string(my_str):
    """Return the Python object described by a JSON string.

    Args:
        my_str (str): the JSON text to read.

    Returns:
        The Python data structure built from the JSON text.
    """
    return json.loads(my_str)
