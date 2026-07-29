# Python - Classes and Objects: Rectangle

## Description

This folder contains ten versions of a `Rectangle` class, `0-rectangle.py`
through `9-rectangle.py`. Each file is a complete, standalone module. By
the last file, `Rectangle` validates its own `width` and `height`,
computes its area and perimeter, prints itself to stdout, can be
recreated with `eval()`, tracks how many instances currently exist, and
can compare or build instances through static and class methods.

No modules are imported anywhere in this project.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Code follows `pycodestyle` (version 2.7.*)
- Every file starts with `#!/usr/bin/python3` and ends with a new line
- Every module and class has a docstring

## Files

| File | What it does |
| --- | --- |
| `0-rectangle.py` | An empty `Rectangle` class - just `class Rectangle:` with a docstring, no attributes. |
| `1-rectangle.py` | Adds `width` and `height` as properties (getter + setter), each validated to be a non-negative `int`. |
| `2-rectangle.py` | Adds `area()` and `perimeter()`. `perimeter()` returns `0` if `width` or `height` is `0`. |
| `3-rectangle.py` | Adds `__str__`, so `print()` and `str()` draw the rectangle using `#`. Returns an empty string if `width` or `height` is `0`. |
| `4-rectangle.py` | Adds `__repr__`, so `repr()` returns a string like `Rectangle(2, 4)` that can be passed to `eval()` to build an equivalent new instance. |
| `5-rectangle.py` | Adds `__del__`, which prints `Bye rectangle...` whenever an instance is deleted. |
| `6-rectangle.py` | Adds the class attribute `number_of_instances`, incremented on creation and decremented on deletion. |
| `7-rectangle.py` | Adds the class attribute `print_symbol` (default `#`). `__str__` now draws the rectangle using `print_symbol` instead of a hardcoded `#`, and `print_symbol` can be any type, not just a string. |
| `8-rectangle.py` | Adds the static method `bigger_or_equal(rect_1, rect_2)`, which returns whichever rectangle has the larger area (or `rect_1` if the areas are equal). |
| `9-rectangle.py` | Adds the class method `square(size)`, which returns a new `Rectangle` with `width == height == size`. |

## Usage examples

### 0-rectangle.py - empty class

```python
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(my_rectangle.__dict__)
```

```
{}
```

### 1-rectangle.py - width and height

```python
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)
```

```
{'_Rectangle__height': 4, '_Rectangle__width': 2}
```

### 2-rectangle.py - area and perimeter

```python
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
```

```
Area: 8 - Perimeter: 12
```

### 3-rectangle.py - printing the rectangle

```python
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle)
```

```
##
##
##
##
```

### 4-rectangle.py - repr() and eval()

```python
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(repr(my_rectangle))

new_rectangle = eval(repr(my_rectangle))
print(new_rectangle)
```

```
Rectangle(2, 4)
##
##
##
##
```

### 5-rectangle.py - deletion message

```python
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
del my_rectangle
```

```
Bye rectangle...
```

### 6-rectangle.py - instance count

```python
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
```

```
2 instances of Rectangle
```

### 7-rectangle.py - custom print symbol

```python
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle = Rectangle(4, 2)
my_rectangle.print_symbol = "&"
print(my_rectangle)
```

```
&&&&
&&&&
```

### 8-rectangle.py - comparing rectangles

```python
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)
print(Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2) is my_rectangle_1)
```

```
True
```

### 9-rectangle.py - building a square

```python
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
```

```
Area: 25 - Perimeter: 20
```

## Author
[RyanGakire](https://github.com/RyanGakire)
