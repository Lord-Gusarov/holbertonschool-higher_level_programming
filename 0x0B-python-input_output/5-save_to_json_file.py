#!/usr/bin/python3
"""Save Object to a file
"""
import json


def save_to_json_file(my_obt, filename):
    """"Writes an Object to a text file, using a JSON representation
    Args:
        my_obt (any): a Python object that we want saved in a file
        filename (str): name of the file to save/write the object to
    """
    with open(filename, 'w') as f:
        json.dump(my_obt, f)
