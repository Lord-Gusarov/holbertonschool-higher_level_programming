#!/usr/bin/python3
"""Unittest module for class Base
"""
from models.base import Base
import unittest
import pep8


class TestBase(unittest.TestCase):
    """tests class Base using unitest
    """

    def test_pep8(self):
        """test that we comply with PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        "tests/test_models/test_base.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def setUpClass(self):
        """Seting up the objects or instances to be tested
        """
        Base._Base__nb_objects = 0
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(100)
        self.b4 = Base()
        self.b5 = Base(200)
        self.b6 = Base("hey")
        self.b7 = Base(-6.5)
        self.b8 = Base()
        self.b9 = Base([1, 2, 3])

    def test_contructors_empty(self):
        """Validates the id's for empty contructors
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b4.id, 3)
        self.assertEqual(self.b8.id, 4)

    def test_constructor_with_ids(self):
        """Validates the id's for non-empty constructors
        """
        self.assertEqual(self.b3.id, 100)
        self.assertEqual(self.b5.id, 200)
        self.assertEqual(self.b6.id, "hey")
        self.assertEqual(self.b7.id, -6.5)
        self.assertEqual(self.b9.id, [1, 2, 3])

    def test_to_json_string(self):
        """testing to_json_string
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'hey': 20}]), '[{"hey": 20}]')
        self.assertEqual(type(Base.to_json_string([{'hey': 20}])), str)

    def test_from_json_string(self):
        """testing from json string
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"hey": 20}]'), [{'hey': 20}])
        self.assertEqual(type(Base.from_json_string('[{"hey": 20}]')), list)
