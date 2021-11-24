#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in matrix[row]:
            print("{:d}".format(matrix[row][column], end=", ")
        print()
