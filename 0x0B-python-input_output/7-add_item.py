#!/usr/bin/python3
"""Task: Load, add, save
Write a script that adds all arguments to a Python list, and then
saves them to a file.
The list must be saved as a JSON representation in a file named add_item.json
"""
import sys
import json

filename = "add_item.json"
alist = []
try:
    with open(filename, 'r') as f:
        alist = json.load(f)
except FileNotFoundError:
    pass

for x in range(1, len(sys.argv)):
        alist.append(sys.argv[x])
with open(filename, 'w') as f:
        json.dump(alist, f)
