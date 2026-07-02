#!/usr/bin/python3
def best_score(a_dictionary):
    """Return the key with the biggest integer value.

    Args:
        a_dictionary (dict): the dictionary to search.

    Returns:
        The key with the highest value, or None if not found.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
