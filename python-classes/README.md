# Python - Classes and Objects

## Description

This folder contains seven versions of a `Square` class, `0-square.py`
through `6-square.py`. Each file is a complete, standalone module. By
the last file, `Square` validates its own `size` and `position`,
computes its area, and prints itself to stdout using `#` characters.

No modules are imported anywhere in this project.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Code follows `pycodestyle` (version 2.7.*)
- Every file starts with `#!/usr/bin/python3` and ends with a new line
- Every module and class has a docstring

## Files

| File | What it adds |
| --- | --- |
| `0-square.py` | An empty `Square` class - just `class Square:` with a docstring, no attributes yet. |
| `1-square.py` | Adds a private attribute `__size`, set in `__init__(self, size)`. No validation yet - it will accept anything. |
| `2-square.py` | Adds validation to `__init__`: `size` must be an `int`, and must be `>= 0`. `size` now defaults to `0` if not given. |
| `3-square.py` | Adds `area()`, which returns `size * size`. |
| `4-square.py` | Turns `size` into a property (getter + setter). Validation now runs from both `__init__` and later assignments to `my_square.size`. |
| `5-square.py` | Adds `my_print()`, which prints the square to stdout using `#` characters (or an empty line if `size` is `0`). |
| `6-square.py` | Adds a second property, `position`, a tuple of 2 positive integers. `my_print()` now uses `position` to add blank lines above the square and spaces to its left. |

## Usage examples

### 0-square.py - empty class

```python
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
```

```
<class '0-square.Square'>
{}
```

### 1-square.py - private size, no checks

```python
Square = __import__('1-square').Square

my_square = Square(3)
print(my_square.__dict__)
```

```
{'_Square__size': 3}
```

`my_square.size` still raises an `AttributeError` here - `__size` is
name-mangled to `_Square__size`, so nothing outside the class can reach
it directly yet.

### 2-square.py - type/value validation

```python
Square = __import__('2-square').Square

Square("3")
```

```
size must be an integer
```

```python
Square(-89)
```

```
size must be >= 0
```

### 3-square.py - area

```python
Square = __import__('3-square').Square

my_square = Square(5)
print("Area: {}".format(my_square.area()))
```

```
Area: 25
```

### 4-square.py - size as a property

```python
Square = __import__('4-square').Square

my_square = Square(89)
my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))
```

```
Area: 9 for size: 3
```

```python
my_square.size = "5 feet"
```

```
size must be an integer
```

### 5-square.py - printing the square

```python
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()
```

```
###
###
###
```

```python
my_square.size = 0
my_square.my_print()
```

```
(empty line)
```

### 6-square.py - printing with a position

```python
Square = __import__('6-square').Square

my_square = Square(3, (1, 1))
my_square.my_print()
```

```

 ###
 ###
 ###
```

The blank line above the square comes from `position[1]` (1 blank
line). The single space before each `###` row comes from `position[0]`
(1 space). No trailing spaces are added after the `#` characters.

## Author
[RyanGakire](https://github.com/RyanGakire)
