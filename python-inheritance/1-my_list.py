#!/usr/bin/python3
"""Module that defines a list subclass able to print itself sorted."""


class MyList(list):
    """A list of integers that can print its elements in ascending order."""

    def print_sorted(self):
        """Print the elements of the list sorted in ascending order.

        The original list is left unchanged.
        """
        print(sorted(self))
