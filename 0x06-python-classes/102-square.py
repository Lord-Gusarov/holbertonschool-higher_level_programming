#!/usr/bin/python3
"""Task4
Write a class Square that defines a square by
 Private instance attribute: size
    property def size(self): to retrieve it
    property setter def size(self, value): to set it
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
        self.size = size

    def __lt__(self, other):
        """How to determine is one Square is less than another one
        Args:
            other: the other Square
        """
        return self.size < other.size

    def __le__(self, other):
        """How to determine is one Square is less or equal to another one
        Args:
            other: the other Square
        """
        return self.size <= other.size

    def __gt__(self, other):
        """How to determine is one Square is greater than another one
        Args:
            other: the other Square
        """
        return self.size > other.size

    def __ge__(self, other):
        """How to determine is one Square is greater or equal to another one
        Args:
            other: the other Square
        """
        return self.size >= other.size

    def __eq__(self, other):
        """How to determine if two Squares are equal
        Args:
            other: the other Square
        """
        return self.size == other.size

    def __ne__(self, other):
        """How to determine if two Squares are NOT equal
        Args:
            other: the other Square
        """
        return self.size != other.size

    def area(self):
        """Calculates the area of the Square

        Returns:
            int: The area of the square
        """
        return (self.__size**2)

    @property
    def size(self):
        """getter method to retrieve the current size of a
        Square class instance

        Retunrs:
            int: size of the Square (>= 0)
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method to set the size of a Square instance,
        if size is not type integer a TypeError exceptios is raised,
        if size is less than 0 a ValueError exception is raised

        Args:
            value (int): new size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
