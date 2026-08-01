# Python - Almost a circle

The last project of the higher level programming track: a small class
hierarchy that ends up saving and loading itself as JSON.

## Classes

| File | Description |
| --- | --- |
| `models/base.py` | `Base`, manages `id` and the JSON serialization |
| `models/rectangle.py` | `Rectangle`, inherits from `Base` |
| `models/square.py` | `Square`, inherits from `Rectangle` |

`Base` holds `to_json_string`, `from_json_string`, `save_to_file`,
`load_from_file` and `create`. `Rectangle` adds validated `width`,
`height`, `x` and `y` attributes, plus `area`, `display`, `update` and
`to_dictionary`. `Square` reuses all of it with a single `size`.

## Tests

Run the whole suite:

```
python3 -m unittest discover tests
```

Run one file:

```
python3 -m unittest tests/test_models/test_base.py
```

## Environment

* Ubuntu 20.04 LTS
* python3 (version 3.8.5)
* pycodestyle (version 2.7.*)
