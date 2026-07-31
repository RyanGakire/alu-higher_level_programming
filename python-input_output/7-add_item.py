#!/usr/bin/python3
"""Script that adds the command line arguments to a list kept in a file.

The list is stored in add_item.json. The file is created the first time
the script runs, and every later run keeps the items already saved.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
