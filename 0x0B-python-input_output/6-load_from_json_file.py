#!/usr/bin/python3
"""Task: Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    """
    with open(filename, encoding="utf-8") as j_file:
        return json.load(j_file)
