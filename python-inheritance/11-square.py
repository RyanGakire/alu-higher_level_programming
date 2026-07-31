#!/usr/bin/python3
"""Module that defines a square that prints its own description."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square that describes itself as a square, not as a rectangle."""

    def __init__(self, size):
        """Create a square after validating its size.

        Args:
            size (int): the length of one side, must be positive.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the description of the square, like [Square] 13/13."""
        return "[Square] {}/{}".format(self.__size, self.__size)
