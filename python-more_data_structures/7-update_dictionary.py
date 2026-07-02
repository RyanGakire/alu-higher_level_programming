#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replace or add a key/value pair in a dictionary.

    Args:
        a_dictionary (dict): the dictionary to update.
        key (str): the key to replace or add.
        value: the value to associate with key.

    Returns:
        dict: the updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
