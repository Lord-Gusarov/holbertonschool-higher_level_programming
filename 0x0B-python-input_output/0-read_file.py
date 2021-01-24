#!/usr/bin/python3
"""Task: Read File
"""


def read_file(filename=""):
    """Read a text file (UTF8) and prints it to stdout
    Args:
        filename (str): name of the file to read
    """
    with open(filename, encoding='UTF8') as f:
        for line in f:
            print(line, end='')
