#!/usr/bin/python3
"""Task: To JSON string
"""


def to_json_string(my_obj):
    """
    Args:
        my_obj (any): a Python Object
    Returns
        str: the JSON representation of an object
    """
    import json
    return json.dumps(my_obj)
