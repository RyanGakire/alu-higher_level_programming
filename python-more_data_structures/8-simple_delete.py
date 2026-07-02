#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Delete a key from a dictionary if it exists.

    Args:
        a_dictionary (dict): the dictionary to update.
        key (str): the key to delete.

    Returns:
        dict: the updated dictionary.
    """
    if a_dictionary is None:
        return a_dictionary
    a_dictionary.pop(key, None)
    return a_dictionary
