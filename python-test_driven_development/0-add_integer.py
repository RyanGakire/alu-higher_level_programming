#!/usr/bin/python3
"""Integers addition module.

This module holds a single function, ``add_integer``, that adds two
numbers together after casting each of them to an integer, so that
floats are truncated before the addition is performed.
"""


def add_integer(a, b=98):
    """Return the addition of ``a`` and ``b`` as an integer.

    Both arguments are casted to integers before being added, which
    means floats are truncated toward zero.

    Args:
        a: The first number, an integer or a float.
        b: The second number, an integer or a float, defaults to 98.

    Returns:
        The integer sum of ``a`` and ``b``.

    Raises:
        TypeError: If ``a`` or ``b`` is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
