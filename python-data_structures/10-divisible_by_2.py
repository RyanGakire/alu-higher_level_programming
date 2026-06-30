#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return []
    result = []
    for n in my_list:
        result.append(n % 2 == 0)
    return result
