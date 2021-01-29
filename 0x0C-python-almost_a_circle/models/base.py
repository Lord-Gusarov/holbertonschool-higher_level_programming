#!/usr/bin/python3
"""Task: Base class
The class defined in this module will be the “base” of all other classes
in this project.
"""
import json
import csv
import turtle
import random


class Base:
    """To manage id attribute in all your future classes and to avoid
    duplicating the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class Contructor
        Args:
            id (int): id of the object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of 'list_dictionaries'
        Returns:
            str: JSON representation of 'list_dictionaries'
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file
        """
        with open(cls.__name__ + ".json", 'w') as jfile:
            list_dict = []
            if list_objs is not None:
                list_dict = [x.to_dictionary() for x in list_objs]
            jfile.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Opens a file for reading and returns a list of the instances
        """
        json_list = None
        try:
            with open(cls.__name__ + ".json") as j_file:
                json_list = cls.from_json_string(j_file.read())
        except FileNotFoundError:
            return []
        return [cls.create(**x) for x in json_list]

    """------------------CVS-------------------"""

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves list_objs to a file using cvs serialization"""
        with open(cls.__name__ + ".csv", mode="w") as f_csv:
            if list_objs is not None:
                attrs = ['id', 'width', 'height', 'size', 'x', 'y']
                list_dict = [item.to_dictionary() for item in list_objs]
                attrs_header = filter(lambda y: y in list_dict[0], attrs)
                writer = csv.DictWriter(f_csv, fieldnames=list(attrs_header))
                writer.writeheader()
                for line in list_dict:
                    writer.writerow(line)

    @classmethod
    def load_from_file_csv(cls):
        """loads from a file using cvs serialization"""
        try:
            with open(cls.__name__ + ".csv") as j_file:
                reader = csv.DictReader(j_file)
                list_dicts = []
                for x in reader:
                    for keys in x:
                        x[keys] = int(x[keys])
                    list_dicts.append(x)
                list_objs = [cls.create(**dic) for dic in list_dicts]
                return list_objs

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window an draws all the Rectangles and Squares
        """
        screen = turtle.Screen()
        screen.bgcolor("lightcyan")
        pen = turtle.Turtle()
        screen.colormode(255)
        pen.pensize(5)

        for list_shapes in [list_rectangles, list_squares]:
            for shape in list_shapes:
                colors = (random.randint(1, 255), random.randint(1, 255),
                          random.randint(1, 255))
                pen.pencolor(colors)
                pen.up()
                pen.setx(shape.x)
                pen.sety(shape.y)
                pen.down()
                for i in range(2):
                    pen.forward(shape.width)
                    pen.right(90)
                    pen.forward(shape.height)
                    pen.right(90)

        screen.exitonclick()
