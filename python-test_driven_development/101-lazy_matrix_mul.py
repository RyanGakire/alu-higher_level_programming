#!/usr/bin/python3
"""Lazy matrix multiplication module.

This module holds a single function, ``lazy_matrix_mul``, that
validates two matrices and then multiplies them with NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the matrix product of ``m_a`` by ``m_b`` computed by NumPy.

    Both matrices are validated before the multiplication is performed,
    in the order given below.

    Args:
        m_a: The first matrix, a list of lists of integers or floats.
        m_b: The second matrix, a list of lists of integers or floats.

    Returns:
        A numpy.ndarray holding the product of ``m_a`` by ``m_b``.

    Raises:
        TypeError: If a matrix is not a list, not a list of lists, holds
            something else than integers or floats, or is not a
            rectangle.
        ValueError: If a matrix is empty, or if the two matrices cannot
            be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return np.matmul(m_a, m_b)
