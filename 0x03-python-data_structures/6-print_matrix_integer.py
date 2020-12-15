#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for ii in range(0, len(matrix[i])):
            print("{:d}".format(matrix[i][ii]), end="")
            if (ii < len(matrix[i]) - 1):
                print(" ", end="")
        print("\n", end="")
