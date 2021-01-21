#!/usr/bin/python3
"""Task: Append to a File
"""


def append_write(filename="", text=""):
    """appends a string to a text file and returns
        the number of characters added
    """
    with open(filename, encoding="utf-8", mode="a") as afile:
        return afile.write(text)
