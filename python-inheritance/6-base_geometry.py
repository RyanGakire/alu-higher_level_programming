#!/usr/bin/python3
"""Module that defines a base class for geometry shapes with an area."""


class BaseGeometry:
    """Base class for geometry shapes.

    The area method must be implemented by every child class.
    """

    def area(self):
        """Raise an Exception because area is not implemented here."""
        raise Exception("area() is not implemented")
