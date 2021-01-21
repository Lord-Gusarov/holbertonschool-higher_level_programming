#!/usr/bin/python3
"""Task: Read file
"""


def read_file(filename=""):
    """reads a text file and prints  it to stdout
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
