#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print a dictionary's key/value pairs sorted by key.

    Only the first-level keys are sorted; nested dictionaries are
    left as-is.

    Args:
        a_dictionary (dict): the dictionary to print.
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
