# Python - Exceptions

This project explores exception handling in Python: catching errors with
`try`/`except`/`finally`, understanding which exceptions built-in operations
raise, and deliberately raising exceptions of a specific type or with a
custom message.

## Files

### `0-safe_print_list.py`
`safe_print_list(my_list=[], x=0)` prints the first `x` elements of a list
on a single line. If `x` is larger than the list, printing simply stops
once the list is exhausted instead of raising an error. Returns the actual
number of elements printed.

### `1-safe_print_integer.py`
`safe_print_integer(value)` prints `value` as an integer using
`"{:d}".format()`. Returns `True` if `value` was a valid integer and got
printed, `False` otherwise (e.g. strings, floats, `None`, lists).

### `2-print_and_count_integer.py`
`safe_print_list_integers(my_list=[], x=0)` prints only the integers found
among the first `x` elements of a list, skipping any other type silently.
Returns the count of integers printed. Unlike `safe_print_list`, this
function does not guard against `x` being larger than the list — that case
is allowed to raise normally.

### `3-safe_division.py`
`safe_print_division(a, b)` divides two integers and always prints the
result inside a `finally` block, prefixed with `Inside result:`. If the
division fails (division by zero), it prints `Error` and returns `None`;
otherwise it returns the division result.

### `4-list_division.py`
`list_division(my_list_1, my_list_2, list_length)` divides two lists
element by element and returns a new list of length `list_length`. Any
element that can't be divided (wrong type, division by zero, or a list
that's too short) results in `0` for that position, along with a printed
message (`wrong type`, `division by 0`, or `out of range`) describing why.

### `5-raise_exception.py`
`raise_exception()` triggers a `TypeError` by attempting an invalid
operation between incompatible types.

### `6-raise_exception_msg.py`
`raise_exception_msg(message="")` raises a `NameError` carrying a custom
message passed in by the caller.
