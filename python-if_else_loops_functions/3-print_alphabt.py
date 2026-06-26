#!/usr/bin/python3
for i in range(26):
    if 97 + i != ord('q') and 97 + i != ord('e'):
        print("{:c}".format(97 + i), end="")
