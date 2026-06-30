#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        line = ""
        for i, n in enumerate(row):
            if i != 0:
                line += " "
            line += "{:d}".format(n)
        print(line)
