# Python - Inheritance

This project is about inheritance in Python. It covers how to look inside an
object, how to check the class an object comes from, and how to build a small
family of classes where each child class reuses and extends its parent.

All the code is written in Python 3 and no module is imported anywhere.

## Requirements

- Ubuntu 20.04 LTS with Python 3.8 or later
- All files end with a new line
- The first line of every file is `#!/usr/bin/python3`
- All files are executable
- The code follows `pycodestyle` (version 2.7.\*)
- Every module, class and function has a real sentence as its documentation
- Allowed editors: `vi`, `vim`, `emacs`

## Files

| File | What it does |
| --- | --- |
| `0-lookup.py` | `lookup(obj)` returns the list of attributes and methods of an object |
| `1-my_list.py` | `MyList` inherits from `list` and can print itself sorted |
| `2-is_same_class.py` | `is_same_class(obj, a_class)` returns `True` only for an exact match |
| `3-is_kind_of_class.py` | `is_kind_of_class(obj, a_class)` also accepts child classes |
| `4-inherits_from.py` | `inherits_from(obj, a_class)` accepts child classes only |
| `5-base_geometry.py` | An empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry` with an `area()` method that raises an exception |
| `7-base_geometry.py` | `BaseGeometry` with `area()` and `integer_validator()` |
| `8-rectangle.py` | `Rectangle` inherits from `BaseGeometry` with a private width and height |
| `9-rectangle.py` | `Rectangle` with a working `area()` and a printable description |
| `10-square.py` | `Square` inherits from `Rectangle` and computes its own area |
| `11-square.py` | `Square` that prints itself as `[Square] <width>/<height>` |
| `tests/1-my_list.txt` | Doctests for `MyList` |
| `tests/7-base_geometry.txt` | Doctests for `BaseGeometry` |

## How to use

The file names start with a number, so they cannot be imported with a normal
`import`. Use `__import__` instead:

```python
#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)
print(s)
print(s.area())
```

Output:

```
[Square] 13/13
169
```

## Tests

The tests are doctest files kept in the `tests` folder. Run them all with:

```
python3 -m doctest ./tests/*
```

Nothing is printed when every test passes. To see each test as it runs, add
the `-v` option:

```
python3 -m doctest ./tests/* -v
```

## Notes

- `integer_validator` uses `type(value) is not int` and not `isinstance`.
  In Python a `bool` is a kind of `int`, so `True` would pass an `isinstance`
  check. The project expects `True` to be refused.
- `inherits_from` returns `False` when the object is an exact instance of the
  class, because the task asks for subclasses only.
- `10-square.py` does not define `__str__`, so a square still prints as
  `[Rectangle] 13/13`. That behaviour changes in `11-square.py`.

## Author
[RyanGakire](https://github.com/RyanGakire)
