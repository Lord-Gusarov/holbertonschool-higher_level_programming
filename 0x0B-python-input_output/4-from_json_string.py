#!/usr/bin/python3
"""Task: From JSON to object
"""
import json


def from_json_string(my_str):
    """ that returns an object (Python data structure) represented
    by a JSON string:
    """
    return json.loads(my_str)
