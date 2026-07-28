#!/usr/bin/python3
"""Module that defines a Rectangle class that can build squares."""


class Rectangle:
    """Represent a rectangle.

    Class Attributes:
        number_of_instances (int): The number of Rectangle instances
            that currently exist.
        print_symbol: The character(s) used to draw the rectangle
            in __str__. Defaults to "#", but can be set to any type.
    """

    number_of_instances = 0
    print_symbol = "#"

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
            int: The width of the rectangle.
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle.

        Returns:
            int: The area of the rectangle (width multiplied by height).
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
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = []
        for row in range(self.__height):
            rows.append(str(self.print_symbol) * self.__width)
        return "\n".join(rows)

    def __repr__(self):
        """Return a string representation that can recreate the rectangle.

        Returns:
            str: A string that, if passed to eval(), creates a new
                Rectangle instance with the same width and height.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when a Rectangle instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger or equal area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle instance.

        Returns:
            Rectangle: rect_1 if its area is greater than or equal to
                the area of rect_2, otherwise rect_2.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size.

        Args:
            size (int): The width and height of the new square
                Rectangle.

        Returns:
            Rectangle: A new Rectangle instance where width and
                height are both equal to size.
        """
        return cls(size, size)
