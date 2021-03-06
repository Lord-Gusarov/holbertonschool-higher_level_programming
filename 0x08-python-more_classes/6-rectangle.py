#!/usr/bin/python3
"""Task 6
::How many instances
This module defines a class 'Rectangle' that defines a rectangle
"""


class Rectangle:
    """Defines a Rectangle, some attributes and functions for Rectangles
    Attributes:
        number_of_intances (int): tracks how many object of this class are
            currently in existance
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Contructor
        Args:
            width (int): must be >= 0
            height (int): must be >= 0
        Returns:
            Rectangle : new object
        """

        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        """Creates a string representation of a Rectangle using '#'
        Returns:
            str : a string representation of a rectangle using '#'
        """
        if self.area == 0:
            return ""
        return (('#' * self.width + '\n') * self.height)[0:-1]

    def __repr__(self):
        """String representation of an object of Class Rectangle
        Returns:
            str : string representation
        """
        return "{}({}, {})".format(self.__class__.__name__,
                                   self.width, self.height)

    @property
    def width(self):
        """getter for private attribute with the same name
        Returns:
            int : the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, newWidth):
        """setter method for private attribute with the same name
        Args:
            newWidth (int): must be >= 0
        """
        if type(newWidth) is not int:
            raise TypeError("width must be an integer")
        if newWidth < 0:
            raise ValueError("width must be >= 0")
        self.__width = newWidth

    @property
    def height(self):
        """getter for private attribute with the same name
        Returns:
            int : the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, newHeight):
        """setter method for private attribute with the same name
        Args:
            newHeight (int): must be >= 0
        """
        if type(newHeight) is not int:
            raise TypeError("height must be an integer")
        if newHeight < 0:
            raise ValueError("height must be >= 0")
        self.__height = newHeight

    def area(self):
        """Calculates the area of a Rectangle
        Returns:
            int : the area, >= 0
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle
        Returns:
            int : the perimeter, >= 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __del__(self):
        """Handling destruction of an instace of class Rectangle"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
