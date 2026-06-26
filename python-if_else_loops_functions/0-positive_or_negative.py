#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0: 
    print("{:d} is positive".format(number))
elif number == 0:
    print("{:d} is zero".format(number))
else:
    print("{:d} is negative".format(number))
