#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list (each counted only once).

    Args:
        my_list (list): a list of integers.

    Returns:
        int: the sum of unique integers.
    """
    return sum(set(my_list))
