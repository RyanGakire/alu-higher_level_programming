#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Print a value as an integer, or report the error.

    Args:
        value: the value to print.

    Returns:
        bool: True if value was printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
