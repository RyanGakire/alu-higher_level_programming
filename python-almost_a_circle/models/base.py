#!/usr/bin/python3
"""Base module.

This module defines the ``Base`` class, the base of all the other
classes of this project, which manages the ``id`` attribute of every
instance and holds the JSON serialization and deserialization helpers.
"""
import json


class Base:
    """Manage the ``id`` attribute of all the classes of the project.

    Attributes:
        __nb_objects: The number of instances created without an ``id``.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id: The identity of the instance. When it is ``None``, the
                number of created objects is incremented and used
                instead.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries: A list of dictionaries.

        Returns:
            The string ``"[]"`` if the list is ``None`` or empty, the
            JSON string representation of the list otherwise.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list held by a JSON string.

        Args:
            json_string: A string representing a list of dictionaries.

        Returns:
            An empty list if the string is ``None`` or empty, the list
            it represents otherwise.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of ``list_objs`` to a file.

        The file is named after the class, for instance
        ``Rectangle.json``, and is overwritten if it already exists.

        Args:
            list_objs: A list of instances inheriting from Base. When it
                is ``None``, an empty list is saved.
        """
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w") as a_file:
            a_file.write(cls.to_json_string(list_dictionaries))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all its attributes already set.

        Args:
            **dictionary: The attributes to set on the new instance.

        Returns:
            A new instance of the class the method is called on.
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from the class JSON file.

        Returns:
            An empty list if the file does not exist, a list of
            instances built from the file otherwise.
        """
        try:
            with open("{}.json".format(cls.__name__), "r") as a_file:
                list_dictionaries = cls.from_json_string(a_file.read())
                return [cls.create(**d) for d in list_dictionaries]
        except IOError:
            return []
