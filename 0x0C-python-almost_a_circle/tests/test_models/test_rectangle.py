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
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(2, 2)
        self.r2 = Rectangle(6, 8, 4)
        self.r3 = Rectangle(300, 1, 1, 1, 200)
        self.r4 = Rectangle(10, 5, 0, 15)

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
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 200)
        self.assertEqual(self.r4.id, 3)

    def test_get_width(self):
        """Test getter method width
        """
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r2.width, 6)
        self.assertEqual(self.r3.width, 300)
        self.assertEqual(self.r4.width, 10)

    def test_set_width(self):
        """Test getter method width
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r5 = Rectangle("hey", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r5 = Rectangle(6.5, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5 = Rectangle(0, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5 = Rectangle(-1, 10)

    def test_get_height(self):
        """Test getter for height
        """
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 8)
        self.assertEqual(self.r3.height, 1)
        self.assertEqual(self.r4.height, 5)

    def test_setter_height(self):
        """Test setter for height
        """

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r5 = Rectangle(1, "hey")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r5 = Rectangle(10, 6.5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r5 = Rectangle(5, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r5 = Rectangle(5, -1)

    def test_constructor_raiases_x_y(self):
        """Tests contructor with invalid X or Y coordinates
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r5 = Rectangle(5, 5, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r5 = Rectangle(5, 5, 10, -5)

    def test_area(self):
        """test area method
        """
        self.assertEqual(self.r1.area(), 4)
        self.assertEqual(self.r2.area(), 48)
        self.assertEqual(self.r3.area(), 300)
