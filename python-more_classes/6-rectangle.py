#!/usr/bin/python3
"""Module that defines a Rectangle class that counts its instances."""


class Rectangle:
    """Represent a rectangle.

    Class Attributes:
        number_of_instances (int): The number of Rectangle instances
            that currently exist.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the current width of the rectangle.

        Returns:
            int: The wifth of the rectange.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(Error) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the current height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle/

        Raises:
            TypeError: If value is not an integer.
            ValueErrorL If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle.

        Returns:
            int: The area of the rectangle (width multiplied by height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Return the current perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or
                height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the printable string representation of the rectangle.

        Returns:
            str: The rectangle drawn with the character '#', or an
                empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0
            return ""
        rows = []
        for row in range(self.__height):
            rows.append("#" * self.__width)
        return "\n".join(rows)

    def __repr__(self):
        """Return a string representation that can recreate the rectangle.

        Returns:
            str: A string that, if passed to eval(), creates a new
                Rectangle instance instance with the same width and height.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when a Rectangle instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
