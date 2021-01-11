#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Testing callss for funct max_integer
    """
    def test_max_integer(self):
        """Asserts the output of certain arguments is as expected
        """
        self.assertEqual(max_integer([-20]), -20)
        """One integer"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        """Multiple integers, MAX at the beggining"""
        self.assertEqual(max_integer([-10, -5, -15]), -5)
        """Just negative integers"""
        self.assertEqual(max_integer([-100, 0, 100]), 100)
        """Mixed positive and negative integers"""
        self.assertEqual(max_integer([0, 0, 0, 0, 0, 0, 1]), 1)
        """Multiple repeated lower number"""
        self.assertEqual(max_integer([-200, 20, 21, 0, 21, -300]), 21)
        """Reapeated Max number"""
        self.assertEqual(max_integer([]), None)
        """Pasing empty list"""
        self.assertEqual(max_integer(), None)
        """Passing no args to the function"""

    def test_max_integer_TypeError(self):
        """Test errors raised by function"""
        self.assertRaises(TypeError, max_integer, [1, 2, None])
        self.assertRaises(TypeError, max_integer, [[34], 41])
