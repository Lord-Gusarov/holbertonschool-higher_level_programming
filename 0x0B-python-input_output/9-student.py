#!/usr/bin/python3
"""Task: Student to JSON
"""


class Student:
    """A student has
    Attributes:
        first_name (str)
        last_name (str)
        age (int)
    """
    def __init__(self, first_name, last_name, age):
        """Student Initializer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dict representation of a Student
        """
        return self.__dict__
