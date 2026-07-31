#!/usr/bin/python3
"""Module that provides a way to inspect any Python object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: any Python object to inspect.

    Returns:
        list: the names of the attributes and methods of obj.
    """
    return dir(obj)
