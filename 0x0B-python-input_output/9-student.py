#!/usr/bin/python3
"""Task: Student to JSON
"""


class Student:
    """A student has first name, last name and age
    """
    def __init__(self, first_name, last_name, age):
        """Initializer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a dictionary representation of a Student
        """
        return self.__dict__
