#!/usr/bin/python3
"""Unittest for amenity file: class and methods"""

import pep8
import unittest
from models import amenity
from models.amenity import Amenity


class TestBaseModelpep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        amen_pep8 = "models/amenity.py"
        test_amen_pep8 = "tests/test_models/test_amenity.py"
        result = style.check_files([amen_pep8, test_amen_pep8])
        self.assertEqual(result.total_errors, 0)


class TestDocsBaseModel(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
