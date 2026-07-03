#!/usr/bin/python3
def magic_calculation(a, b):
    """Perform the calculation described by the original bytecode.

    Args:
        a (int): first value.
        b (int): second value.

    Returns:
        int/float: the calculated result.
    """
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except Exception:
            result = b + a
            break

    return result
