#!/usr/bin/python3
"""Task: Exact same object
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the
    specified class ; otherwise False.
    Args:
        obj (any): an object
        a_class: any python Class, may be user defined
    Retruns:
        boolean: True if the object is instance of the specified class
    """
    return type(obj) is a_class
