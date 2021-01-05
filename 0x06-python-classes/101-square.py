#!/usr/bin/python3
"""Task101
Write a class Square that defines a square by
 Private instance attribute: size
    property def size(self): to retrieve it
    property setter def size(self, value): to set it
Private instance attribute: position:
    property def position(self): to retrieve it
    property setter def position(self, value): to set it:
    position must be a tuple of 2 positive integers, otherwise
    raise a TypeError exception
Instantiation with optional size: def __init__(self, size=0):
    Size must be an integer, otherwise raise a TypeError exception with the
    message size must be an integer
    If size is less than 0, raise a ValueError exception with the
    message size must be >= 0
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square
with the character #:
    if size is equal to 0, print an empty line
SQUARE IS NOW PRINTABLE, same output as my_print()
"""


class Square:
    """Defines a Square class with an integer size equal or
    greater than zero
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializer, validates given size for correct type
        and for correct value. If one of these is not correct,
        and exception is raised


        Args:
            size (int): must be an integer greater or equal to zero
            position (tuple): lenght of 2 and positive integers or an
                exception is raised
        """
        self.size = size
        self.position = position

    def __str__(self):
        """String representation of a Square instance with
        the character '#'
        Returns:
            str: string representation
        """
        s = ""
        if self.__size > 0:
            for nl in range(0, self.__position[1]):
                s += '\n'
            for a in range(0, self.__size):
                for spaces in range(0, self.__position[0]):
                    s += ' '
                for b in range(0, self.__size):
                    s += '#'
                s += '\n'
            s = s[:-1]
        return s

    def area(self):
        """Calculates the area of the Square

        Returns:
            int: The area of the square
        """
        return (self.__size**2)

    def my_print(self):
        """prints the square to stdout with the character #
        If a position has been set, it will be displaced
        accordingly
        """

        if self.__size == 0:
            print("")
        else:
            for nl in range(0, self.__position[1]):
                print("")
            for a in range(0, self.__size):
                for s in range(0, self.__position[0]):
                    print(" ", end="")
                for b in range(0, self.__size):
                    print("#", end="")
                print("")

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

    @property
    def position(self):
        """getter method for the 2 elements position tuple

        Returns:
            tuple: position tuple of len 2
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter method for position tuple

        If the given value is not a tuple of exactly 2 positive integers
        a TypeError exception is raised.

        Args:
            value (tuple): 2 positive integers
        """
        flag = False
        if type(value) is tuple:
            if len(value) == 2:
                if type(value[0]) is int and value[0] >= 0:
                    if type(value[1]) is int and value[1] >= 0:
                        flag = True
                        self.__position = value
        if flag is False:
            raise TypeError("position must be a tuple of 2 positive integers")
