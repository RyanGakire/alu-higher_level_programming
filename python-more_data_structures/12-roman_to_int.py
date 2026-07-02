#!/usr/bin/python3
def roman_to_int(roman_string):
    """Convert a Roman numeral string to an integer.

    Args:
        roman_string (str): the Roman numeral to convert.

    Returns:
        int: the integer value, or 0 if input is invalid.
    """
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for symbol in reversed(roman_string):
        value = values.get(symbol, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total
