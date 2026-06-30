#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return ""
    result = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            result += ch
        return result
