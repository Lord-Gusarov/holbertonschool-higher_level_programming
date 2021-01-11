#!/usr/bin/python3
"""Divide a Matrix
Matrix must be a list of lists of ints or floats, otherwise raise a TypeError
Each row of the matrix must be of the same size, otherwise raise a TypeError
All elements should be divided by div, rounded to 2 decimal places
You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    """Divides all element of 'matrix' by 'div', returns a new matrix
    Args:
        matrix (list of list of ints or floats): matrix of integers to divide
        div (int, float): non-zero number to divide all elements of the matrix
    Returns:
        matrix: a new list of list of ints
    """
    if type(matrix) is not list or \
            any(map(lambda x: type(x) is not list or
                any(map(lambda a: type(a) not in [int, float], x)), matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of " +
                        "integers/floats")
    l_len = len(matrix[0])
    if any(map(lambda x: len(x) != l_len, matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda l: list(map(lambda i: round(i / div,
                                                       2), l)), matrix))
