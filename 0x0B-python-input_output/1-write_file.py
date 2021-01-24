#!/usr/bin/python3
"""Task: Write to a file
"""


def write_file(filename="", text=""):
    """writes to a file, overtwiting it if it exist
    Args:
        filename (str): desire name of the output file
        text (str): what is to be written
    """
    with open(filename, 'w') as f:
        return f.write(text)
