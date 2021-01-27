#!/usr/bin/python3
"""Unittest module for class Rectangle
"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
import pep8


class TestRectangle(unittest.TestCase):
    """tests class Rectangle using unitest
    """

    @classmethod
    def setUpClass(self):
        """Seting up the objects or instances to be tested
        """
        self.r1 = Rectangle(2, 2, 0, 0, 7)
        self.r2 = Rectangle(6, 8, 4, 6, 100)
        self.r3 = Rectangle(300, 1, 1, 1, 200)
        self.r4 = Rectangle(10, 5, 0, 15, 300)

    def test_pep8(self):
        """test that we comply with PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py',
                                        "tests/test_models/test_rectangle.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_id(self):
        """Test the ids
        """
        self.assertEqual(self.r1.id, 7)
        self.assertEqual(self.r2.id, 100)
        self.assertEqual(self.r3.id, 200)
        self.assertEqual(self.r4.id, 300)

    def test_get_width(self):
        """Test getter method width
        """
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r2.width, 6)
        self.assertEqual(self.r3.width, 300)

    def test_set_width(self):
        """Test getter method width
        """
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r2.width, 6)
        self.assertEqual(self.r3.width, 300)
        r5 = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r5.width = "hey"
        with self.assertRaises(TypeError):
            r5.width = 6.5
        with self.assertRaises(ValueError):
            r5.width = 0

    def test_area(self):
        """test area method
        """
        self.assertEqual(self.r1.area(), 4)
        self.assertEqual(self.r2.area(), 48)
        self.assertEqual(self.r3.area(), 300)
