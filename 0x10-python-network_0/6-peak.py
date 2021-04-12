#!/usr/bin/python3
"""Defines a function to find a Peak"""


def find_peak(list_of_integers):
    """Finds a peak in a list of integers
    Args:
        list_of_integers (list): a list of integers
    Return:
        int or None
    """
    if type(list_of_integers) is not list:
        return None
    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return l[1]
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]

    for idx in range(1, length):
        if (list_of_integers[idx - 1] < list_of_integers[idx]
        and list_of_integers[idx] > list_of_integers[idx + 1]):
            return list_of_integers[idx]

    return list_of_integers[0]
