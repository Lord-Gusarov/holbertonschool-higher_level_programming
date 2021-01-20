#!/usr/bin/python3
"""Task: Integer validator
"""


class BaseGeometry():
    """Basic Geometry manipulations
    """
    def area(self):
        """method not define yet
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates 'value'
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
