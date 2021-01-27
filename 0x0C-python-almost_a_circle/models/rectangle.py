#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from
the Base class in model.base
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class with private attributes but public id inherited
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle object Initializer
        Args:
            width: rectangle's width
            height: rectangle's height
            x: coordinate 'x'
            y: coordinate 'y'
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """String representation of a Rectangle Object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    @property
    def width(self):
        """getter for private attribute 'width'
        Returns:
            int: current width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private attribute 'width'
        Args:
            value (int): new width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for private attribute 'height'
        Returns:
            int: current height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private attribute 'height'
        Args:
            value (int): new height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for private attribute 'x'
        Returns:
            int: current x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter for private attribute 'x'
        Args:
            value (int): new x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for private attribute 'y'
        Returns:
            int: current y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for private attribute 'y'
        Args:
            value (int): new y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the Area
        Returns:
            int: width * height
        """
        return self.width * self.height

    def display(self):
        """that prints in stdout the Rectangle instance with the character #
        """
        print('\n' * self.y, end="")
        print((" " * self.x + ("#" * self.width) + '\n') * self.height, end="")

    def update(self, *args, **kwargs):
        """Variable argument count funct, assigns an argument to each attribute
        """
        cnt = len(args)
        if cnt > 0:
            self.id = args[0]
            if cnt > 1:
                self.width = args[1]
                if cnt > 2:
                    self.height = args[2]
                    if cnt > 3:
                        self.x = args[3]
                        if cnt > 4:
                            self.y = args[4]
        elif kwargs is not None:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle object
        Returns:
            dict: a dictionary
        """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
