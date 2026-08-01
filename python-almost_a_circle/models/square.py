#!/usr/bin/python3
"""Square module.

This module defines the ``Square`` class, a special ``Rectangle`` whose
width and height are always equal.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square, a rectangle of equal width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size: The size of a side of the square.
            x: The horizontal offset of the square.
            y: The vertical offset of the square.
            id: The identity of the square.

        Raises:
            TypeError: If an argument is not an integer.
            ValueError: If size is under or equal to 0, or if x or y is
                under 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of a side of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and the height of the square to the same value."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign arguments to the attributes of the square.

        Args:
            *args: The values of id, size, x and y, in that order.
            **kwargs: The attributes to set, skipped when args is not
                empty.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for name, value in zip(attributes, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
