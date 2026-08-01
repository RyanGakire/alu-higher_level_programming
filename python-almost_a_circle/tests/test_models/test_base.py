#!/usr/bin/python3
"""Unittests for the Base class."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseId(unittest.TestCase):
    """Test the id given to a Base instance."""

    def test_id_is_incremented(self):
        """Two instances without an id get two consecutive ids."""
        first = Base()
        second = Base()
        self.assertEqual(second.id, first.id + 1)

    def test_given_id(self):
        """A given id is used as it is."""
        self.assertEqual(Base(12).id, 12)

    def test_given_id_does_not_increment(self):
        """A given id does not change the counter of instances."""
        before = Base()
        Base(89)
        after = Base()
        self.assertEqual(after.id, before.id + 1)

    def test_none_id(self):
        """An id of None falls back on the counter of instances."""
        self.assertIsNotNone(Base(None).id)

    def test_negative_id(self):
        """A negative id is accepted."""
        self.assertEqual(Base(-5).id, -5)

    def test_zero_id(self):
        """An id of 0 is used as it is and not treated as None."""
        self.assertEqual(Base(0).id, 0)

    def test_string_id(self):
        """The type of the id is not checked."""
        self.assertEqual(Base("hello").id, "hello")

    def test_no_extra_attribute(self):
        """A Base instance only holds an id."""
        self.assertEqual(list(Base(1).__dict__.keys()), ["id"])

    def test_nb_objects_is_private(self):
        """The counter of instances is not reachable from outside."""
        with self.assertRaises(AttributeError):
            print(Base(1).__nb_objects)


class TestBaseToJsonString(unittest.TestCase):
    """Test the to_json_string static method."""

    def test_none(self):
        """None gives an empty list representation."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """An empty list gives an empty list representation."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_one_dictionary(self):
        """A list of one dictionary is serialized."""
        dictionary = {"id": 1, "width": 2}
        self.assertEqual(json.loads(Base.to_json_string([dictionary])),
                         [dictionary])

    def test_two_dictionaries(self):
        """A list of two dictionaries keeps both of them."""
        dictionaries = [{"id": 1}, {"id": 2}]
        self.assertEqual(json.loads(Base.to_json_string(dictionaries)),
                         dictionaries)

    def test_return_type(self):
        """The returned value is a string."""
        self.assertIs(type(Base.to_json_string([{"id": 1}])), str)


class TestBaseFromJsonString(unittest.TestCase):
    """Test the from_json_string static method."""

    def test_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """An empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_empty_list_string(self):
        """The string of an empty list gives an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_one_dictionary(self):
        """A string holding one dictionary is deserialized."""
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])

    def test_return_type(self):
        """The returned value is a list."""
        self.assertIs(type(Base.from_json_string('[{"id": 1}]')), list)

    def test_round_trip(self):
        """Serializing then deserializing gives the first list back."""
        dictionaries = [{"id": 89, "width": 10, "height": 4}]
        json_string = Base.to_json_string(dictionaries)
        self.assertEqual(Base.from_json_string(json_string), dictionaries)


class TestBaseSaveToFile(unittest.TestCase):
    """Test the save_to_file class method."""

    def tearDown(self):
        """Remove the files written by the tests."""
        for name in ("Rectangle.json", "Square.json", "Base.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_file_is_created(self):
        """The file is named after the class."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_none(self):
        """None saves an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_empty_list(self):
        """An empty list saves an empty list."""
        Square.save_to_file([])
        with open("Square.json") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_content(self):
        """The file holds the dictionaries of the given instances."""
        rectangle = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([rectangle])
        with open("Rectangle.json") as a_file:
            self.assertEqual(json.load(a_file), [rectangle.to_dictionary()])

    def test_overwrite(self):
        """Saving twice overwrites the file."""
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        Rectangle.save_to_file([Rectangle(5, 6)])
        with open("Rectangle.json") as a_file:
            self.assertEqual(len(json.load(a_file)), 1)

    def test_square_file(self):
        """A list of squares is saved in Square.json."""
        Square.save_to_file([Square(5)])
        self.assertTrue(os.path.exists("Square.json"))


class TestBaseCreate(unittest.TestCase):
    """Test the create class method."""

    def test_rectangle(self):
        """A rectangle is built from a dictionary."""
        rectangle = Rectangle.create(**{"id": 89, "width": 1, "height": 2,
                                        "x": 3, "y": 4})
        self.assertEqual(str(rectangle), "[Rectangle] (89) 3/4 - 1/2")

    def test_square(self):
        """A square is built from a dictionary."""
        square = Square.create(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(str(square), "[Square] (89) 2/3 - 1")

    def test_type(self):
        """The instance is of the class the method is called on."""
        self.assertIs(type(Rectangle.create(**{"width": 1, "height": 2})),
                      Rectangle)

    def test_new_instance(self):
        """The instance created is not the one given."""
        rectangle = Rectangle(3, 5, 1)
        other = Rectangle.create(**rectangle.to_dictionary())
        self.assertIsNot(rectangle, other)

    def test_partial_dictionary(self):
        """Attributes missing from the dictionary keep their dummy value."""
        rectangle = Rectangle.create(**{"id": 7})
        self.assertEqual(rectangle.id, 7)


class TestBaseLoadFromFile(unittest.TestCase):
    """Test the load_from_file class method."""

    def tearDown(self):
        """Remove the files written by the tests."""
        for name in ("Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_no_file(self):
        """A missing file gives an empty list."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rectangles(self):
        """The rectangles saved are loaded back."""
        rectangles = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
        Rectangle.save_to_file(rectangles)
        loaded = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in loaded],
                         [str(r) for r in rectangles])

    def test_squares(self):
        """The squares saved are loaded back."""
        squares = [Square(5), Square(7, 9, 1)]
        Square.save_to_file(squares)
        loaded = Square.load_from_file()
        self.assertEqual([str(s) for s in loaded], [str(s) for s in squares])

    def test_type_of_instances(self):
        """The instances loaded are of the calling class."""
        Square.save_to_file([Square(5)])
        self.assertIs(type(Square.load_from_file()[0]), Square)

    def test_new_instances(self):
        """The instances loaded are not the ones saved."""
        rectangle = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([rectangle])
        self.assertIsNot(Rectangle.load_from_file()[0], rectangle)

    def test_empty_file(self):
        """A file holding an empty list gives an empty list."""
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])


class TestBaseDocumentation(unittest.TestCase):
    """Test the documentation of the module and of the class."""

    def test_module_documentation(self):
        """The module has a documentation."""
        self.assertTrue(len(__import__("models.base").base.__doc__) > 10)

    def test_class_documentation(self):
        """The class has a documentation."""
        self.assertTrue(len(Base.__doc__) > 10)

    def test_methods_documentation(self):
        """Every method of the class has a documentation."""
        for name in ("to_json_string", "from_json_string", "save_to_file",
                     "create", "load_from_file", "__init__"):
            self.assertTrue(len(getattr(Base, name).__doc__) > 10)


if __name__ == "__main__":
    unittest.main()
