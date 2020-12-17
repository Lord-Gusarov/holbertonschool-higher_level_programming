#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_M = []
    for l in matrix:
        n_M.append(list(map(lambda x: x**2, l)))
    return n_M
