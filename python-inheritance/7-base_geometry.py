#!/usr/bin/python3
"""Module that defines a base geometry class with an integer validator."""


class BaseGeometry:
    """Base class for geometry shapes.

    It provides an area method to override and a validator that makes
    sure a value is a positive integer.
    """

    def area(self):
        """Raise an Exception because area is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is an integer greater than 0.

        Args:
            name (str): the name of the value, used in error messages.
            value: the value to check.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
