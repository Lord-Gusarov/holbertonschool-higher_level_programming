#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    r = my_list[::-1]
    for x in r:
        print("{:d}".format(x))
