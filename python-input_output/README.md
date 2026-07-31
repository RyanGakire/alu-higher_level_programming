# Python - Input/Output

This project is about reading and writing files in Python, and about JSON.
JSON is a simple text format used to save an object to disk and to build the
same object again later. The last task is a small interview exercise about
Pascal's triangle.

All the code is written in Python 3.

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
| `0-read_file.py` | `read_file(filename="")` prints the whole content of a text file |
| `1-write_file.py` | `write_file(filename="", text="")` writes a string to a file and returns the number of characters written |
| `2-append_write.py` | `append_write(filename="", text="")` adds a string at the end of a file |
| `3-to_json_string.py` | `to_json_string(my_obj)` returns the JSON text of an object |
| `4-from_json_string.py` | `from_json_string(my_str)` returns the object described by JSON text |
| `5-save_to_json_file.py` | `save_to_json_file(my_obj, filename)` saves an object to a file as JSON |
| `6-load_from_json_file.py` | `load_from_json_file(filename)` builds an object from a JSON file |
| `7-add_item.py` | Script that adds its command line arguments to a list saved in `add_item.json` |
| `8-class_to_json.py` | `class_to_json(obj)` returns the attributes of an instance as a dictionary |
| `9-student.py` | `Student` class with a `to_json()` method |
| `10-student.py` | `Student` whose `to_json(attrs=None)` can return only some attributes |
| `11-student.py` | `Student` that can also be rebuilt with `reload_from_json(json)` |
| `12-pascal_triangle.py` | `pascal_triangle(n)` returns Pascal's triangle as a list of lists |

## How to use

The file names start with a number, so they cannot be imported with a normal
`import`. Use `__import__` instead:

```python
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
```

Task 7 is a script, so it runs straight from the shell:

```
./7-add_item.py Best School
cat add_item.json
["Best", "School"]
```

## Notes

- Tasks 0, 1, 2, 8, 9, 10, 11 and 12 import nothing at all. Only the JSON
  tasks use the `json` module, and task 7 uses `sys` to read the arguments.
- Every file task uses the `with` statement, so the file is always closed
  properly, even when an error happens.
- In task 5 the file is opened before the object is turned into JSON. So when
  the object cannot be serialised, like a set, the file is still created but
  stays empty. That is what the example output shows.
- In task 10, `attrs` is only used when it really is a list of strings.
  Anything else means all the attributes are returned.

## Author
[RyanGakire](https://github.com/RyanGakire)
