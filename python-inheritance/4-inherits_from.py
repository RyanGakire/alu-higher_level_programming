#!/usr/bin/python3
"""Module that checks if an object is an instance of a subclass only."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited from
    a_class, directly or indirectly.

    Return False if obj is exactly an instance of a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
