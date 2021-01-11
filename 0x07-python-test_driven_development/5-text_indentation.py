#!/usr/bin/python3
"""Task: Text indentation
Write a function that prints a text with 2 new lines after each of
    these characters: ., ? and :
There should be no space at the beginning or at the end of each printed line
You are not allowed to import any module
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of
    these characters: ., ? and :
    Args:
        text (str): text to print indented
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    t_break = True
    for x in text.strip():
        if t_break and x == ' ':
            continue
        print(x, end="")
        t_break = False
        if x in ['.', '?', ':']:
            print('\n')
            t_break = True
