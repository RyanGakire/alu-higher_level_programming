#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Execute a function safely and return its result.

    Args:
        fct: the function to execute.
        *args: the arguments to pass to the function.

    Returns:
        The result of fct(*args), or None if an exception occurred.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
