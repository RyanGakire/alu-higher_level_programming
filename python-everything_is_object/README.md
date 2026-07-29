# Python - Everything is Object

## Description

This folder contains one-line answer files exploring how Python
handles objects, identity, and mutability under the hood - the
difference between two variables holding *equal* values versus
holding the *same* object, and what that means for integers, strings,
and lists.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Each answer file contains exactly one line, no shebang
- Each file ends with a new line

## Files

| File | Answer | What it's about |
| --- | --- | --- |
| `0-file` | `type` | The function that prints an object's type. |
| `1-file` | `id` | The function that returns an object's identifier (its memory address in CPython). |
| `2-file` | `No` | `a = 89`, `b = 100` - different values, different objects. |
| `3-file` | `Yes` | `a = 89`, `b = 89` - CPython caches small integers (-5 to 256), so both point to the same cached object. |
| `4-file` | `Yes` | `a = 89`, `b = a` - direct aliasing, same object. |
| `5-file` | `No` | `a = 89`, `b = a + 1` - `a + 1` creates a new value, a different object from `a`. |
| `6-file` | `True` | `s2 = s1`, then `s1 == s2` - same content. |
| `7-file` | `True` | `s2 = s1`, then `s1 is s2` - same object (aliasing). |
| `8-file` | `True` | Two separately-written `"Best School"` literals, `s1 == s2` - same content. |
| `9-file` | `False` | Same two literals, `s1 is s2` - different objects. See note below. |
| `10-file` | `True` | Two separately-built lists with the same contents, `l1 == l2`. |
| `11-file` | `False` | Same two separately-built lists, `l1 is l2` - equal content, but different objects. |
| `12-file` | `True` | `l2 = l1`, then `l1 == l2` - same object, so naturally equal content too. |
| `13-file` | `True` | `l2 = l1`, then `l1 is l2` - same object (aliasing). |
| `14-file` | `[1, 2, 3, 4]` | `l2 = l1`, then `l1.append(4)` - since `l2` and `l1` are the same list object, the change shows up through both names. |

### A note on `9-file`

Task 7 and task 9 look similar but test different things. Task 7 uses
`s2 = s1` - direct aliasing, so `is` is trivially `True`. Task 9
creates two *separate* string literals with the same text. Whether
those end up as the same object depends on whether Python's compiler
merges identical literals, which only happens within a single block of
code compiled together - typed as separate lines at the `>>> ` prompt,
each line compiles independently, so no merging happens. CPython also
only auto-interns strings that look like identifiers (letters, digits,
underscores); `"Best School"` has a space, so it's excluded either way.
Both effects point the same direction, which is why `is` returns
`False` here even though `==` returns `True`.

## Author
[RyanGakire](http://Github.com/RyanGakire)
