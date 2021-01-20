#!/usr/bin/python3
"""Task: My List
Write a class MyList that inherits from list
"""


class MyList(list):
    """A class derived from class 'list'
    """
    def print_sorted(self):
        """print a MyList instance in ascending order
        """

        print(sorted(self))
