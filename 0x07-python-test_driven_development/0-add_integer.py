#!/usr/bin/python3
"""
Test Driven Development, Task 0
Write a function that adds 2 integers.
You are not allowed to import any module
"""


def add_integer(a, b=98):
    """Exceptions thrown if the args types are not 'int' or 'float'
    a, b (int, float): the two integers to add
    Returns: int: the addittion of the integers"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
