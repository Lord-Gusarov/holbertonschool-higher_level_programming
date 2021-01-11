#!/usr/bin/python3
"""Task 1
::Real definition of a rectangle
This module defines a class 'Rectangle' that defines a rectangle
"""


class Rectangle:
    """Defines a Rectangle, some attributes and functions for Rectangles"""
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
