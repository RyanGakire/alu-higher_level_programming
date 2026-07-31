#!/usr/bin/python3
"""Module that checks if an object comes from a class or its parents."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass of it.

    Otherwise return False.
    """
    return isinstance(obj, a_class)
