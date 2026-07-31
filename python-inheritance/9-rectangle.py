#!/usr/bin/python3
"""Module that defines a rectangle that can compute and print itself."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle that knows its area and how to describe itself."""

    def __init__(self, width, height):
        """Create a rectangle after validating its width and height.

        Args:
            width (int): the width of the rectangle, must be positive.
            height (int): the height of the rectangle, must be positive.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the description of the rectangle, like [Rectangle] 3/5."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
