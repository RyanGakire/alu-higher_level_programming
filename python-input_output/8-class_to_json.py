#!/usr/bin/python3
"""Module that describes an instance of a class as a dictionary."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON.

    Only the attributes of the instance are returned, and they are all
    simple types: list, dictionary, string, integer and boolean.

    Args:
        obj: an instance of a class.

    Returns:
        dict: the attributes of the instance with their values.
    """
    return obj.__dict__.copy()
