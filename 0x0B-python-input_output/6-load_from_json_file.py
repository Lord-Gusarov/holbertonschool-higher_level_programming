#!/usr/bin/python3
"""Task: Create object from a JSON file
"""
import json
from io import StringIO


def load_from_json_file(filename):
    """Creates an Object from a JSON file
    Args:
        filename (str): name of the file to read from
    Returns:
        any: a Python Object
    """
    with open(filename) as f:
        return json.load(f)
