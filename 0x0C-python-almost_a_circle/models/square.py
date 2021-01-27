#!/usr/bin/python3
"""Task: And now, the Square!
Modules defines a Square class that inherits from the Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class than Inherits from Rectangle and Rectangle inherits
    from Base
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square Object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a Square Object
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Getter method for size in a Square
        """
        return self.width

    @size.setter
    def size(self, size):
        """Sets the dimension of a Squared Rectangle
        Args:
            size (int): the dimension of a squared Rectangle
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the attributes of a Square
        """
        if args is not None and len(args) is not 0:
            l_args = list(args)
            if len(args) > 1:
                l_args.insert(1, args[1])
                """So that size is repeated for width and height attributes"""
            super().update(*l_args)

        else:
            super().update(**kwargs)
            if "size" in kwargs:
                self.size = kwargs["size"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square
        Returns:
            dict: a dictionary
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
