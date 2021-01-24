#!/usr/bin/python3
"""Task: Student to disk and reload
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

    def to_json(self, attrs=None):
        """Retrieves a dict representation of a Student.
        >If attrs is a list of strings, only attribute names contained in this
         list must be retrieved.
        > Otherwise, all attributes must be retrieved
        """
        if type(attrs) is list and all(type(x) is str for x in attrs):
            d = dict()
            for a in attrs:
                if a in self.__dict__:
                    d[a] = self.__dict__[a]
            return d
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        Args:
            json (dict): atrribute name with vale pair
        """
        for k, v in json:
            self.__dict__[k] = v
