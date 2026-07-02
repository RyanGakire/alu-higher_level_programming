#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list.

    Args:
        my_list (list): the initial list.
        search: the element to replace.
        replace: the new element.

    Returns:
        list: a new list with all occurrences of search replaced.
    """
    return [replace if item == search else item for item in my_list]
