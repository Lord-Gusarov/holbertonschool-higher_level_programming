#!/usr/bin/python3
"""Task: Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initializer
        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
        """
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width

    def area(self):
        """area of the Rectangle
        Returns:
            int: area > 0
        """
        return self.__width * self.__height

    def __str__(self):
        """String represenation
        Returns:
            str: a string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
