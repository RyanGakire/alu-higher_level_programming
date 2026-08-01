#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """The maximum is the last element of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """The maximum is found in the middle of a list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """The maximum is the first element of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        """A list of one element returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Calling without argument uses the empty default and returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """The maximum of negative numbers is the closest one to zero."""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_signs(self):
        """Positive and negative numbers are compared correctly."""
        self.assertEqual(max_integer([-10, 5, -3, 2]), 5)

    def test_duplicated_max(self):
        """A maximum appearing several times is still returned once."""
        self.assertEqual(max_integer([3, 9, 9, 1]), 9)

    def test_all_equal(self):
        """A list of identical elements returns that element."""
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_floats(self):
        """Floats are compared like integers."""
        self.assertEqual(max_integer([1.5, 3.25, 2.0]), 3.25)

    def test_mixed_numbers(self):
        """Integers and floats can be mixed."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_strings(self):
        """A list of strings returns the greatest string."""
        self.assertEqual(max_integer(["apple", "car", "boat"]), "car")

    def test_single_string(self):
        """A string is a list of characters, the greatest one is returned."""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_not_comparable(self):
        """Comparing elements of different types raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

    def test_none_argument(self):
        """None has no length, so a TypeError is raised."""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
