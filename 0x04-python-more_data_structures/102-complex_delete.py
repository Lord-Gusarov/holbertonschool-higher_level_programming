#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in a_dictionary.copy().items():
        if v == value:
            a_dictionary.pop(k)
    return a_dictionary
