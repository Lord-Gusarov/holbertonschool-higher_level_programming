#!/usr/bin/python3
"""Task: Only sub class of
"""


def inherits_from(obj, a_class):
    """returns True  if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    Args:
        obj (any): an object
        a_class: any python Class, may be user defined
    Retruns:
        boolean: True if the object is subclass of the specified class
    """
    if type(obj) == a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
