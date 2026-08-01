#!/usr/bin/python3
"""Lazy matrix multiplication module.

This module holds a single function, ``lazy_matrix_mul``, that
multiplies two matrices with NumPy and lets NumPy raise its own
exceptions when the matrices are not valid.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the matrix product of ``m_a`` by ``m_b`` computed by NumPy.

    Args:
        m_a: The first matrix, a list of lists of integers or floats.
        m_b: The second matrix, a list of lists of integers or floats.

    Returns:
        A numpy.ndarray holding the product of ``m_a`` by ``m_b``.

    Raises:
        TypeError: If NumPy cannot build an array of numbers out of an
            argument.
        ValueError: If the shapes of the two matrices do not allow a
            multiplication.
    """
    return np.matmul(m_a, m_b)
