#!/usr/bin/python3
def no_c(my _string):
    result = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            result += ch
        return result
