#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        for x in sorted(a_dictionary.keys()):
            print("{}: {}".format(x, a_dictionary[x]))
