#!/usr/bin/python3
"""Module that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle of n rows as a list of lists of integers.

    Each number is the sum of the two numbers above it. An empty list is
    returned when n is 0 or less.

    Args:
        n (int): the number of rows wanted.

    Returns:
        list: the rows of the triangle, each one a list of integers.
    """
    triangle = []
    if n <= 0:
        return triangle
    for row_number in range(n):
        row = [1]
        if triangle:
            previous = triangle[-1]
            for i in range(len(previous) - 1):
                row.append(previous[i] + previous[i + 1])
            row.append(1)
        triangle.append(row)
    return triangle
