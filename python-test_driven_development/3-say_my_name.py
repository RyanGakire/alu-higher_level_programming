#!/usr/bin/python3
"""Name printing module.

This module holds a single function, ``say_my_name``, that prints a
full name built from a first name and an optional last name.
"""


def say_my_name(first_name, last_name=""):
    """Print ``My name is <first name> <last name>``.

    Args:
        first_name: The first name to print, a string.
        last_name: The last name to print, a string, defaults to "".

    Raises:
        TypeError: If ``first_name`` or ``last_name`` is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
