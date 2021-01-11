#!/usr/bin/python3
"""
Task: Print square
This module defines a function that prints a square
using the '#' character.
"""


def print_square(size):
    """Prints a square of specified size
    Args:
        size (int): size of the square, if not an integer or less
            than zero Exceptions will be raised
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("#" * size)
