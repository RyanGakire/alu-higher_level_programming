#!/usr/bin/python3
"""Matrix division module.

This module holds a single function, ``matrix_divided``, that divides
every element of a matrix by a number and returns a new matrix, leaving
the matrix it was given untouched.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all elements of ``matrix`` divided by ``div``.

    Every result is rounded to 2 decimal places and the original matrix
    is not modified.

    Args:
        matrix: A list of lists of integers or floats, with rows of
            equal size.
        div: The number to divide each element by.

    Returns:
        A new matrix holding the divided values.

    Raises:
        TypeError: If ``matrix`` is not a list of lists of integers or
            floats, if its rows do not all have the same size, or if
            ``div`` is not a number.
        ZeroDivisionError: If ``div`` is equal to 0.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(error)
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(error)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
