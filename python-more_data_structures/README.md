# Python - More Data Structures

A collection of small Python utilities for working with matrices, lists,
sets, and dictionaries, plus a Roman numeral to integer converter.

## Author

Prince Gakire

## `0-square_matrix_simple.py`
Squares every number in a 2D matrix.

```python
>>> square_matrix_simple([[1, 2], [3, 4]])
[[1, 4], [9, 16]]
```

## `1-search_replace.py`
Swaps out every occurrence of one value in a list for another.

```python
>>> search_replace([1, 2, 3, 2], 2, 9)
[1, 9, 3, 9]
```

## `2-uniq_add.py`
Sums the distinct numbers in a list — duplicates only count once.

```python
>>> uniq_add([1, 2, 2, 3])
6
```

## `3-common_elements.py`
Finds the values two sets have in common.

```python
>>> common_elements({1, 2, 3}, {2, 3, 4})
{2, 3}
```

## `4-only_diff_elements.py`
Finds the values that belong to only one of two sets, not both.

```python
>>> only_diff_elements({1, 2, 3}, {2, 3, 4})
{1, 4}
```

## `5-number_keys.py`
Counts how many keys a dictionary has.

```python
>>> number_keys({"a": 1, "b": 2})
2
```

## `6-print_sorted_dictionary.py`
Prints a dictionary's entries in alphabetical order by key.

```python
>>> print_sorted_dictionary({"b": 2, "a": 1})
a: 1
b: 2
```

## `7-update_dictionary.py`
Sets a key's value in a dictionary — adding it if it's new, overwriting it
if it already exists.

```python
>>> update_dictionary({"a": 1}, "b", 2)
{'a': 1, 'b': 2}
```

## `8-simple_delete.py`
Removes a key from a dictionary if it's there; does nothing otherwise.

```python
>>> simple_delete({"a": 1, "b": 2}, "b")
{'a': 1}
```

## `9-multiply_by_2.py`
Doubles every value in a dictionary, returning a new one.

```python
>>> multiply_by_2({"a": 1, "b": 2})
{'a': 2, 'b': 4}
```

## `10-best_score.py`
Finds the key tied to the highest value in a dictionary.

```python
>>> best_score({"alice": 90, "bob": 75})
'alice'
```

## `11-multiply_list_map.py`
Multiplies every value in a list by a number, using `map` instead of a loop.

```python
>>> multiply_list_map([1, 2, 3], 2)
[2, 4, 6]
```

## `12-roman_to_int.py`
Converts a Roman numeral string into its integer value.

```python
>>> roman_to_int("MCMXCIV")
1994
```
