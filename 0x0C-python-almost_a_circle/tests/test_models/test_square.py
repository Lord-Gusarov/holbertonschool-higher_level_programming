#!/usr/bin/python3
"""Unittest module for class Rectangle
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import pep8


class TestSquare(unittest.TestCase):
    """tests class Rectangle using unitest
    """

    @classmethod
    def setUpClass(self):
        """Seting up the objects or instances to be tested
        """
        Base.__nb_objects = 0
        self.s1 = Square(2, 2, 0, 0)
        self.s2 = Square(6, 8, 4, 6)
        self.s3 = Square(300, 1, 1, 200)
        self.s4 = Square(10, 5, 3, 15)

    def test_pep8(self):
        """test that we comply with PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py',
                                        "tests/test_models/test_square.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_id(self):
        """Test the ids
        """
        self.assertEqual(self.s1.id, 0)
        self.assertEqual(self.s2.id, 6)
        self.assertEqual(self.s3.id, 200)
        self.assertEqual(self.s4.id, 15)

    def test_get_width(self):
        """Test getter method width
        """
        self.assertEqual(self.s1.width, 2)
        self.assertEqual(self.s2.width, 6)
        self.assertEqual(self.s3.width, 300)

    def test_set_width(self):
        """Test getter method width
        """
        self.assertEqual(self.s1.width, 2)
        self.assertEqual(self.s2.width, 6)
        self.assertEqual(self.s3.width, 300)
        s5 = Square(1, 1)
        with self.assertRaises(TypeError):
            s5.size = "hey"
        with self.assertRaises(TypeError):
            s5.width = 6.5
        with self.assertRaises(ValueError):
            s5.size = 0

    def test_area(self):
        """test area method
        """
        self.assertEqual(self.s1.area(), 4)
        self.assertEqual(self.s2.area(), 36)
        self.assertEqual(self.s3.area(), 90000)
