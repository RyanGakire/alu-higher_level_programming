#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide a by b and print the result, even if it fails.

    Args:
        a (int): the dividend.
        b (int): the divisor.

    Returns:
        float: the result of the division, or None if it failed.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
