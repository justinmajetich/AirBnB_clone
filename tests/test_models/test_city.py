#!/usr/bin/python3
"""tests for city class"""
import pycodestyle
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class TestCityDoc(unittest.TestCase):
    """check City documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(City.__doc__) > 0)


class TestCityPycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycodestyle(self):
        """tests pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/city.py']).total_errors,
            0, "PEP 8 style issues found"
        )


class test_City(test_basemodel):
    """test city class"""

    def __init__(self, *args, **kwargs):
        """test constructor for city"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """test state id from city"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """test name from city"""
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()
