#!/usr/bin/python3
"""Task: Lookup
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object
    Args:
        obj (any): any object
    Returns:
        list: of all attribtutes and methods
    """
    return dir(obj)
