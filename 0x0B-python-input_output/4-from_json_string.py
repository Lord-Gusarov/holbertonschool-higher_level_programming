#!/usr/bin/python3
"""Task: From JSON string to Object
"""


def from_json_string(my_str):
    """
    Args:
        my_str (str): JSON string representation of an object
    Returns:
        object: a Python data structure instance
    """
    import json
    return json.load(my_str)
