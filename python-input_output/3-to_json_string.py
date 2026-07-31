#!/usr/bin/python3
"""Module that turns a Python object into a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string.

    Args:
        my_obj: the object to convert.

    Returns:
        str: the JSON text of the object.
    """
    return json.dumps(my_obj)
