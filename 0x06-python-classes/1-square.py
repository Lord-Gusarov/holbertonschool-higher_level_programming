#!/usr/bin/python3
"""
Task 1
Write a class Square that defines a square by
>Private instance attribute: size
>Instantiation with size (no type/value verification)
>You are not allowed to import any module
"""


class Square:
    """
    A class that defines a Square

    """

    def __init__(self, size):
        """Initializes and instance of class Square
        takes the size and sets it for the new instance

        Args:
            size: size for the new instance
        """
        self.__size = size
