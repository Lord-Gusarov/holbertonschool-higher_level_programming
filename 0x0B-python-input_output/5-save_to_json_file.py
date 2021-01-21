#!/usr/bin/python3
"""Task: Save Object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation
    """
    with open(filename, encoding="utf-8", mode="w") as j_file:
        j_file.write(json.dumps(my_obj))
