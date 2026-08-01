#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Test the creation of a Rectangle."""

    def test_is_a_base(self):
        """A Rectangle is a Base."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_two_arguments(self):
        """Width and height are enough to build a rectangle."""
        rectangle = Rectangle(10, 2)
        self.assertEqual((rectangle.width, rectangle.height), (10, 2))

    def test_default_offsets(self):
        """The offsets default to 0."""
        rectangle = Rectangle(10, 2)
        self.assertEqual((rectangle.x, rectangle.y), (0, 0))

    def test_all_arguments(self):
        """All the arguments are assigned to the right attribute."""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((rectangle.width, rectangle.height, rectangle.x,
                          rectangle.y, rectangle.id), (1, 2, 3, 4, 5))

    def test_id_is_incremented(self):
        """Rectangles without an id get consecutive ids."""
        first = Rectangle(1, 1)
        second = Rectangle(1, 1)
        self.assertEqual(second.id, first.id + 1)

    def test_no_argument(self):
        """Width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument(self):
        """Height is required."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_private_width(self):
        """The width attribute is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1).__width)


class TestRectangleValidation(unittest.TestCase):
    """Test the validation done by the setters."""

    def test_width_not_an_integer(self):
        """A width that is not an integer is refused."""
        for value in ("2", 2.5, None, [2], {}, (2,), True):
            with self.assertRaises(TypeError) as context:
                Rectangle(value, 2)
            self.assertEqual(str(context.exception),
                             "width must be an integer")

    def test_height_not_an_integer(self):
        """A height that is not an integer is refused."""
        for value in ("2", 2.5, None, [2], {}, (2,)):
            with self.assertRaises(TypeError) as context:
                Rectangle(2, value)
            self.assertEqual(str(context.exception),
                             "height must be an integer")

    def test_x_not_an_integer(self):
        """An x that is not an integer is refused."""
        for value in ("2", 2.5, None, {}):
            with self.assertRaises(TypeError) as context:
                Rectangle(2, 2, value)
            self.assertEqual(str(context.exception), "x must be an integer")

    def test_y_not_an_integer(self):
        """A y that is not an integer is refused."""
        for value in ("2", 2.5, None, {}):
            with self.assertRaises(TypeError) as context:
                Rectangle(2, 2, 0, value)
            self.assertEqual(str(context.exception), "y must be an integer")

    def test_width_not_positive(self):
        """A width under or equal to 0 is refused."""
        for value in (0, -1, -10):
            with self.assertRaises(ValueError) as context:
                Rectangle(value, 2)
            self.assertEqual(str(context.exception), "width must be > 0")

    def test_height_not_positive(self):
        """A height under or equal to 0 is refused."""
        for value in (0, -1, -10):
            with self.assertRaises(ValueError) as context:
                Rectangle(2, value)
            self.assertEqual(str(context.exception), "height must be > 0")

    def test_x_negative(self):
        """A negative x is refused."""
        with self.assertRaises(ValueError) as context:
            Rectangle(2, 2, -1)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_y_negative(self):
        """A negative y is refused."""
        with self.assertRaises(ValueError) as context:
            Rectangle(2, 2, 3, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_x_zero_is_valid(self):
        """An x of 0 is valid."""
        self.assertEqual(Rectangle(2, 2, 0).x, 0)

    def test_width_before_height(self):
        """The width is validated before the height."""
        with self.assertRaises(TypeError) as context:
            Rectangle("1", "2")
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_setter_validation(self):
        """The setters validate the values assigned after creation."""
        rectangle = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            rectangle.width = -10
        with self.assertRaises(TypeError):
            rectangle.x = {}


class TestRectangleArea(unittest.TestCase):
    """Test the area method."""

    def test_area(self):
        """The area is the width multiplied by the height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_area_of_a_big_rectangle(self):
        """The area of a large rectangle is computed as well."""
        self.assertEqual(Rectangle(999, 999).area(), 998001)

    def test_area_of_one_by_one(self):
        """The smallest rectangle has an area of 1."""
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_area_after_update(self):
        """The area follows the attributes of the rectangle."""
        rectangle = Rectangle(3, 2)
        rectangle.width = 5
        self.assertEqual(rectangle.area(), 10)

    def test_area_takes_no_argument(self):
        """The area method takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(3, 2).area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Test the display method."""

    def display_of(self, rectangle):
        """Return what a rectangle prints."""
        output = io.StringIO()
        with redirect_stdout(output):
            rectangle.display()
        return output.getvalue()

    def test_display(self):
        """A rectangle is drawn with the # character."""
        self.assertEqual(self.display_of(Rectangle(2, 2)), "##\n##\n")

    def test_display_one_by_one(self):
        """The smallest rectangle is a single character."""
        self.assertEqual(self.display_of(Rectangle(1, 1)), "#\n")

    def test_display_with_x(self):
        """The x offset is drawn with spaces."""
        self.assertEqual(self.display_of(Rectangle(3, 2, 1)),
                         " ###\n ###\n")

    def test_display_with_y(self):
        """The y offset is drawn with new lines."""
        self.assertEqual(self.display_of(Rectangle(2, 1, 0, 2)),
                         "\n\n##\n")

    def test_display_with_x_and_y(self):
        """Both offsets are honoured."""
        self.assertEqual(self.display_of(Rectangle(2, 3, 2, 2)),
                         "\n\n  ##\n  ##\n  ##\n")

    def test_display_takes_no_argument(self):
        """The display method takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(2, 2).display(1)


class TestRectangleStr(unittest.TestCase):
    """Test the __str__ method."""

    def test_str(self):
        """A rectangle prints its id, offsets and size."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")

    def test_str_with_default_offsets(self):
        """The default offsets are printed too."""
        self.assertEqual(str(Rectangle(5, 5, 1, 0, 7)),
                         "[Rectangle] (7) 1/0 - 5/5")

    def test_str_after_update(self):
        """The string representation follows the attributes."""
        rectangle = Rectangle(4, 6, 2, 1, 12)
        rectangle.width = 8
        self.assertEqual(str(rectangle), "[Rectangle] (12) 2/1 - 8/6")


class TestRectangleUpdate(unittest.TestCase):
    """Test the update method."""

    def setUp(self):
        """Build a rectangle used by the tests."""
        self.rectangle = Rectangle(10, 10, 10, 10, 1)

    def test_update_id(self):
        """The first argument is the id."""
        self.rectangle.update(89)
        self.assertEqual(str(self.rectangle), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_width(self):
        """The second argument is the width."""
        self.rectangle.update(89, 2)
        self.assertEqual(str(self.rectangle), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_all(self):
        """The five arguments are assigned in order."""
        self.rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_no_argument(self):
        """Updating with nothing changes nothing."""
        self.rectangle.update()
        self.assertEqual(str(self.rectangle), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_too_many_arguments(self):
        """Arguments after the fifth one are ignored."""
        self.rectangle.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(self.rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_validates(self):
        """The values given are validated."""
        with self.assertRaises(ValueError):
            self.rectangle.update(89, -2)

    def test_update_kwargs(self):
        """Keyworded arguments are assigned to their attribute."""
        self.rectangle.update(height=1)
        self.assertEqual(str(self.rectangle), "[Rectangle] (1) 10/10 - 10/1")

    def test_update_several_kwargs(self):
        """Several keyworded arguments are assigned."""
        self.rectangle.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(self.rectangle), "[Rectangle] (89) 3/1 - 2/10")

    def test_kwargs_skipped_when_args(self):
        """Keyworded arguments are skipped when args is not empty."""
        self.rectangle.update(89, width=1)
        self.assertEqual(str(self.rectangle), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_kwargs_validates(self):
        """The keyworded values are validated too."""
        with self.assertRaises(TypeError):
            self.rectangle.update(width="1")


class TestRectangleToDictionary(unittest.TestCase):
    """Test the to_dictionary method."""

    def test_keys(self):
        """The dictionary holds the five attributes."""
        self.assertEqual(sorted(Rectangle(10, 2, 1, 9).to_dictionary().keys()),
                         ["height", "id", "width", "x", "y"])

    def test_values(self):
        """The dictionary holds the values of the rectangle."""
        rectangle = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(rectangle.to_dictionary(),
                         {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_type(self):
        """A dictionary is returned."""
        self.assertIs(type(Rectangle(10, 2).to_dictionary()), dict)

    def test_used_by_update(self):
        """The dictionary can be given back to update."""
        rectangle = Rectangle(10, 2, 1, 9)
        other = Rectangle(1, 1)
        other.update(**rectangle.to_dictionary())
        self.assertEqual(str(other), str(rectangle))

    def test_not_the_same_object(self):
        """Two rectangles holding the same values are not equal."""
        rectangle = Rectangle(10, 2, 1, 9)
        other = Rectangle(1, 1)
        other.update(**rectangle.to_dictionary())
        self.assertNotEqual(rectangle, other)


class TestRectangleDocumentation(unittest.TestCase):
    """Test the documentation of the module and of the class."""

    def test_module_documentation(self):
        """The module has a documentation."""
        module = __import__("models.rectangle").rectangle
        self.assertTrue(len(module.__doc__) > 10)

    def test_class_documentation(self):
        """The class has a documentation."""
        self.assertTrue(len(Rectangle.__doc__) > 10)

    def test_methods_documentation(self):
        """Every method of the class has a documentation."""
        for name in ("__init__", "area", "display", "update", "to_dictionary",
                     "__str__"):
            self.assertTrue(len(getattr(Rectangle, name).__doc__) > 10)


if __name__ == "__main__":
    unittest.main()
