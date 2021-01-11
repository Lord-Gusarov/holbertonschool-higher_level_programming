#!/usr/bin/python3
"""Say my name
Write a function that prints My name is <first name> <last name>
first_name and last_name must be strings otherwise, raise a TypeError exception
You are not allowed to import any module
"""


def say_my_name(first_name, last_name=""):
    """ Prints My name is <fist_name> <last_name>
    Args:
        first_name (str): a string
        last_name (str): a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
