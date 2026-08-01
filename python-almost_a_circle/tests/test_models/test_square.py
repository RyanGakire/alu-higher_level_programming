#!/usr/bin/python3
"""Unittests for the Square class."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Test the creation of a Square."""

    def test_is_a_rectangle(self):
        """A Square is a Rectangle."""
        self.assertIsInstance(Square(5), Rectangle)

    def test_is_a_base(self):
        """A Square is a Base."""
        self.assertIsInstance(Square(5), Base)

    def test_size_sets_both_sides(self):
        """The size is used as width and as height."""
        square = Square(5)
        self.assertEqual((square.width, square.height), (5, 5))

    def test_default_offsets(self):
        """The offsets default to 0."""
        square = Square(5)
        self.assertEqual((square.x, square.y), (0, 0))

    def test_all_arguments(self):
        """All the arguments are assigned to the right attribute."""
        square = Square(1, 2, 3, 4)
        self.assertEqual((square.size, square.x, square.y, square.id),
                         (1, 2, 3, 4))

    def test_id_is_incremented(self):
        """Squares without an id get consecutive ids."""
        first = Square(1)
        second = Square(1)
        self.assertEqual(second.id, first.id + 1)

    def test_no_argument(self):
        """The size is required."""
        with self.assertRaises(TypeError):
            Square()

    def test_no_new_attribute(self):
        """A square holds the attributes of a rectangle only."""
        self.assertEqual(sorted(Square(5).__dict__.keys()),
                         ["_Rectangle__height", "_Rectangle__width",
                          "_Rectangle__x", "_Rectangle__y", "id"])


class TestSquareValidation(unittest.TestCase):
    """Test the validation inherited from Rectangle."""

    def test_size_not_an_integer(self):
        """A size that is not an integer is refused, as a width."""
        for value in ("5", 5.5, None, [5], {}):
            with self.assertRaises(TypeError) as context:
                Square(value)
            self.assertEqual(str(context.exception),
                             "width must be an integer")

    def test_size_not_positive(self):
        """A size under or equal to 0 is refused, as a width."""
        for value in (0, -1):
            with self.assertRaises(ValueError) as context:
                Square(value)
            self.assertEqual(str(context.exception), "width must be > 0")

    def test_x_not_an_integer(self):
        """An x that is not an integer is refused."""
        with self.assertRaises(TypeError) as context:
            Square(5, "1")
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_y_not_an_integer(self):
        """A y that is not an integer is refused."""
        for value in ("3", 3.5, None, {}):
            with self.assertRaises(TypeError) as context:
                Square(1, 2, value)
            self.assertEqual(str(context.exception), "y must be an integer")

    def test_x_negative(self):
        """A negative x is refused."""
        for value in (-2, -10):
            with self.assertRaises(ValueError) as context:
                Square(1, value)
            self.assertEqual(str(context.exception), "x must be >= 0")

    def test_y_negative(self):
        """A negative y is refused."""
        for value in (-1, -3):
            with self.assertRaises(ValueError) as context:
                Square(1, 2, value)
            self.assertEqual(str(context.exception), "y must be >= 0")

    def test_size_zero(self):
        """A size of 0 is refused."""
        with self.assertRaises(ValueError) as context:
            Square(0)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_all_arguments_valid(self):
        """A square built with the four arguments keeps them."""
        square = Square(1, 2, 3, 4)
        self.assertEqual((square.size, square.x, square.y, square.id),
                         (1, 2, 3, 4))

    def test_size_setter_validation(self):
        """The size setter validates with the width messages."""
        square = Square(5)
        with self.assertRaises(TypeError) as context:
            square.size = "9"
        self.assertEqual(str(context.exception), "width must be an integer")


class TestSquareSize(unittest.TestCase):
    """Test the size getter and setter."""

    def test_getter(self):
        """The size is the width of the square."""
        self.assertEqual(Square(5).size, 5)

    def test_setter(self):
        """The setter changes both sides of the square."""
        square = Square(5)
        square.size = 10
        self.assertEqual((square.width, square.height), (10, 10))

    def test_setter_changes_str(self):
        """The string representation follows the size."""
        square = Square(5, 0, 0, 1)
        square.size = 10
        self.assertEqual(str(square), "[Square] (1) 0/0 - 10")

    def test_size_follows_width(self):
        """Changing the width changes the size."""
        square = Square(5)
        square.width = 7
        self.assertEqual(square.size, 7)


class TestSquareArea(unittest.TestCase):
    """Test the area method inherited from Rectangle."""

    def test_area(self):
        """The area is the size squared."""
        self.assertEqual(Square(5).area(), 25)

    def test_area_of_one(self):
        """The smallest square has an area of 1."""
        self.assertEqual(Square(1).area(), 1)

    def test_area_after_resize(self):
        """The area follows the size."""
        square = Square(2)
        square.size = 3
        self.assertEqual(square.area(), 9)


class TestSquareDisplay(unittest.TestCase):
    """Test the display method inherited from Rectangle."""

    def display_of(self, square):
        """Return what a square prints."""
        output = io.StringIO()
        with redirect_stdout(output):
            square.display()
        return output.getvalue()

    def test_display(self):
        """A square is drawn with the # character."""
        self.assertEqual(self.display_of(Square(2)), "##\n##\n")

    def test_display_with_x(self):
        """The x offset is drawn with spaces."""
        self.assertEqual(self.display_of(Square(2, 2)), "  ##\n  ##\n")

    def test_display_with_x_and_y(self):
        """Both offsets are honoured."""
        self.assertEqual(self.display_of(Square(3, 1, 3)),
                         "\n\n\n ###\n ###\n ###\n")


class TestSquareStr(unittest.TestCase):
    """Test the __str__ method."""

    def test_str(self):
        """A square prints its id, offsets and size."""
        self.assertEqual(str(Square(5, 0, 0, 1)), "[Square] (1) 0/0 - 5")

    def test_str_with_offsets(self):
        """The offsets are printed."""
        self.assertEqual(str(Square(3, 1, 3, 7)), "[Square] (7) 1/3 - 3")


class TestSquareUpdate(unittest.TestCase):
    """Test the update method."""

    def setUp(self):
        """Build a square used by the tests."""
        self.square = Square(5, 0, 0, 1)

    def test_update_id(self):
        """The first argument is the id."""
        self.square.update(10)
        self.assertEqual(str(self.square), "[Square] (10) 0/0 - 5")

    def test_update_size(self):
        """The second argument is the size."""
        self.square.update(1, 2)
        self.assertEqual(str(self.square), "[Square] (1) 0/0 - 2")

    def test_update_x(self):
        """The third argument is x."""
        self.square.update(1, 2, 3)
        self.assertEqual(str(self.square), "[Square] (1) 3/0 - 2")

    def test_update_all(self):
        """The four arguments are assigned in order."""
        self.square.update(1, 2, 3, 4)
        self.assertEqual(str(self.square), "[Square] (1) 3/4 - 2")

    def test_update_no_argument(self):
        """Updating with nothing changes nothing."""
        self.square.update()
        self.assertEqual(str(self.square), "[Square] (1) 0/0 - 5")

    def test_update_kwargs(self):
        """Keyworded arguments are assigned to their attribute."""
        self.square.update(x=12)
        self.assertEqual(str(self.square), "[Square] (1) 12/0 - 5")

    def test_update_several_kwargs(self):
        """Several keyworded arguments are assigned."""
        self.square.update(size=7, id=89, y=1)
        self.assertEqual(str(self.square), "[Square] (89) 0/1 - 7")

    def test_kwargs_skipped_when_args(self):
        """Keyworded arguments are skipped when args is not empty."""
        self.square.update(10, size=1)
        self.assertEqual(str(self.square), "[Square] (10) 0/0 - 5")

    def test_update_validates(self):
        """The values given are validated."""
        with self.assertRaises(ValueError):
            self.square.update(1, -2)


class TestSquareToDictionary(unittest.TestCase):
    """Test the to_dictionary method."""

    def test_keys(self):
        """The dictionary holds the four attributes."""
        self.assertEqual(sorted(Square(10, 2, 1).to_dictionary().keys()),
                         ["id", "size", "x", "y"])

    def test_values(self):
        """The dictionary holds the values of the square."""
        self.assertEqual(Square(10, 2, 1, 1).to_dictionary(),
                         {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_type(self):
        """A dictionary is returned."""
        self.assertIs(type(Square(10).to_dictionary()), dict)

    def test_used_by_update(self):
        """The dictionary can be given back to update."""
        square = Square(10, 2, 1)
        other = Square(1, 1)
        other.update(**square.to_dictionary())
        self.assertEqual(str(other), str(square))

    def test_no_width_key(self):
        """The dictionary of a square holds a size, not a width."""
        self.assertNotIn("width", Square(10).to_dictionary())


class TestSquareDocumentation(unittest.TestCase):
    """Test the documentation of the module and of the class."""

    def test_module_documentation(self):
        """The module has a documentation."""
        module = __import__("models.square").square
        self.assertTrue(len(module.__doc__) > 10)

    def test_class_documentation(self):
        """The class has a documentation."""
        self.assertTrue(len(Square.__doc__) > 10)

    def test_methods_documentation(self):
        """Every method of the class has a documentation."""
        for name in ("__init__", "update", "to_dictionary", "__str__"):
            self.assertTrue(len(getattr(Square, name).__doc__) > 10)


if __name__ == "__main__":
    unittest.main()
