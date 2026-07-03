#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the integers among the first x elements of a list.

    Args:
        my_list (list): the list to read from.
        x (int): the number of elements to access.

    Returns:
        int: the real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
