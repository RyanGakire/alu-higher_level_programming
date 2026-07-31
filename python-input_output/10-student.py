#!/usr/bin/python3
"""Module that defines a student able to filter its own description."""


class Student:
    """A student that can describe itself, in full or in part."""

    def __init__(self, first_name, last_name, age):
        """Create a student.

        Args:
            first_name (str): the first name of the student.
            last_name (str): the last name of the student.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary description of the student.

        Args:
            attrs (list): names of the attributes to keep. If it is not
                a list of strings, every attribute is returned.

        Returns:
            dict: the chosen attributes with their values.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()
