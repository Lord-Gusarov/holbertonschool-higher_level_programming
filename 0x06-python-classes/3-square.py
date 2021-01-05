#!/usr/bin/python3
"""Task3
Write a class Square that defines a square by
 Private instance attribute: size
 Instantiation with optional size: def __init__(self, size=0):
    Size must be an integer, otherwise raise a TypeError exception with the
    message size must be an integer
    If size is less than 0, raise a ValueError exception with the
    message size must be >= 0
 Public instance method: def area(self): that returns the current square area
"""


class Square:
    """Defines a Square class with an integer size equal or
    greater than zero
    """

    def __init__(self, size=0):
        """Initializer, validates given size for correct type
        and fo correct value. If one of these is not correct,
        and exception is raised

        Args:
            size (int): must be an integer greater or equal to zero
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the Square

        Returns:
            int: The area of the square
        """
        return (self.__size**2)
