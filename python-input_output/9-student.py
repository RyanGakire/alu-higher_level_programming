#!/usr/bin/python3
"""Module that defines a student who can describe itself."""


class Student:
    """A student with a first name, a last name and an age."""

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

    def to_json(self):
        """Return the dictionary description of the student."""
        return self.__dict__.copy()
