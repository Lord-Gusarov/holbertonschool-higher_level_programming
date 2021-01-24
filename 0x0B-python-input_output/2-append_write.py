#!/usr/bin/python3
"""Task: Append to a file
"""


def append_write(filename="", text=""):
    """appends tex to a text file and returns the number of chars added
    Args:
        filename (str): name of the file to append text to
        text (str): what we want appended to the file
    Returns:
        int: number of chars added
    """
    with open(filename, 'a') as f:
        return f.write(text)
