#!/usr/bin/python3
"""Square printing module.

This module holds a single function, ``print_square``, that prints a
square of a given size using the ``#`` character.
"""


def print_square(size):
    """Print a square of ``#`` characters of side ``size``.

    Args:
        size: The length of a side of the square, a positive integer.

    Raises:
        TypeError: If ``size`` is not an integer.
        ValueError: If ``size`` is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
