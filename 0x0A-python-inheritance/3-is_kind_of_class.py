#!/usr/bin/python3
"""Task: Same class or inherit from
"""


def is_same_class(obj, a_class):
    """returns True  if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class;
    otherwise False
    Args:
        obj (any): an object
        a_class: any python Class, may be user defined
    Retruns:
        boolean: True if the object is instance of the specified class
    """
    return isinstance(obj, a_class)
