#!/usr/bin/python3
"""Task: Student to JSON with filter
"""


class Student:
    """ class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        """
        if (type(attrs) is list and
           all(list(map(lambda x: type(x) == str, attrs)))):
            my_dict = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    value = getattr(self, attr)
                    my_dict.update({attr: value})
            return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """object from JSON rep
        """
        for k, v in sorted(json.items()):
            self.__dict__[k] = v