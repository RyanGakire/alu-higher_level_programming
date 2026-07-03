#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide two lists element by element.

    Args:
        my_list_1 (list): the list of numerators.
        my_list_2 (list): the list of denominators.
        list_length (int): the length of the result list.

    Returns:
        list: a new list containing the division results.
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
