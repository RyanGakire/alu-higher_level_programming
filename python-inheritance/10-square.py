#!/usr/bin/python3
"""Module that defines a square based on the Rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square, which is a rectangle with equal sides."""

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
