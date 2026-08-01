# Python - Test-driven development

Small functions written test-first, with doctests in `tests/` and one
unittest file.

| File | Description |
| --- | --- |
| `0-add_integer.py` | Adds 2 integers, casting floats to integers |
| `2-matrix_divided.py` | Divides all elements of a matrix, rounded to 2 decimals |
| `3-say_my_name.py` | Prints `My name is <first name> <last name>` |
| `4-print_square.py` | Prints a square of `#` characters |
| `5-text_indentation.py` | Prints a text with 2 new lines after `.`, `?` and `:` |
| `6-max_integer.py` | Returns the max integer of a list, `None` if empty |

## Tests

Doctests:

```
python3 -m doctest ./tests/*.txt -v
```

Unittest:

```
python3 -m unittest tests.6-max_integer_test
```

## Environment

* Ubuntu 20.04 LTS
* python3 (version 3.8.5)
* pycodestyle (version 2.7.*)
