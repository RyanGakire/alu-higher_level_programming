#!/usr/bin/python3
"""Module that defines a rectangle based on BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a private width and a private height."""

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
