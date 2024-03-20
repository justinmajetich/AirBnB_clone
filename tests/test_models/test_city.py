#!/usr/bin/python3
"""Test cases for the City class."""

# Importing necessary modules
import unittest
import os
import pycodestyle
from models.city import City
from models.base_model import BaseModel

class TestCityAttributes(unittest.TestCase):
    """Test cases for the attributes of the City class."""
    
    def __init__(self, *args, **kwargs):
        """Initialize test cases."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id_type(self):
        """Test if the 'state_id' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name_type(self):
        """Test if the 'name' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.name), str)

class TestCityMethods(unittest.TestCase):
    """Test cases for the methods of the City class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the test class."""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """Tear down for the test class."""
        del cls.city

    def tearDown(self):
        """Tear down for each test."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_conformance(self):
        """Test for PEP8 style conformance."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    def test_docstring_presence(self):
        """Test for the presence of docstrings."""
        self.assertIsNotNone(City.__doc__)

    def test_attribute_presence(self):
        """Test for the presence of attributes."""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_subclass_check(self):
        """Test if City is a subclass of BaseModel."""
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def test_attribute_types(self):
        """Test for the types of attributes."""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_method(self):
        """Test for the save method."""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_method(self):
        """Test for the to_dict method."""
        self.assertTrue('to_dict' in dir(self.city))

if __name__ == "__main__":
    unittest.main()
