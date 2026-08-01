#!/usr/bin/python3
"""Rectangle module.

This module defines the ``Rectangle`` class, which inherits from
``Base`` and holds a width, a height and the offsets used to draw it.
"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle defined by a width, a height and offsets."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: The horizontal offset of the rectangle.
            y: The vertical offset of the rectangle.
            id: The identity of the rectangle.

        Raises:
            TypeError: If an argument is not an integer.
            ValueError: If width or height is under or equal to 0, or if
                x or y is under 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle after validating it."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle after validating it."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: The horizontal offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal offset of the rectangle after validating it."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: The vertical offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical offset of the rectangle after validating it."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the ``#`` character, honouring x and y."""
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Assign arguments to the attributes of the rectangle.

        Args:
            *args: The values of id, width, height, x and y, in that
                order.
            **kwargs: The attributes to set, skipped when args is not
                empty.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for name, value in zip(attributes, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
