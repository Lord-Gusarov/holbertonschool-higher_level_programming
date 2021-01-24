#!/usr/bin/python3
"""Task: From JSON string to Object
"""
import json
from io import StringIO


def from_json_string(my_str):
    """
    Args:
        my_str (str): JSON string representation of an object
    Returns:
        object: a Python data structure instance
    """
    return json.load(StringIO(my_str))
