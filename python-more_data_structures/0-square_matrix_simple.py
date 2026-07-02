#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the square of every integer in a 2D matrix.
    Args:
        matrix (list): a 2 dimensional list of integers.

    Returns:
        list: a new matrix with squared values, same size as matrix.
    """
    return [[value ** 2 for value in row] for row in matrix]
