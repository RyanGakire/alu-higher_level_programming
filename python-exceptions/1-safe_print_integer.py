#!/usr/bin/python3
def safe_print_integer(value):
    """Print a value formatted as an integer.

    Args:
        value: the value to print.

    Returns:
        bool: True if value was printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
