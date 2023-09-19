#!/usr/bin/python3
"""This tests for module clase City """
import unittest
import os
import pep8
from os import getenv
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """This tests for class City that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """This initializes the test process """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @classmethod
    def setUpClass(cls):
        """This sets up test"""
        cls.city = City()
        cls.city.name = "CA"
        cls.city.state_id = "LA"

    @classmethod
    def teardown(cls):
        """This will tear it down at the end of the test"""
        del cls.city

    def tearDown(self):
        """This tears down the set up"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_state_id(self):
        """This tests for the functionality of the state_id """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Tests the functionality of the name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_checking_for_docstring_City(self):
        """checking for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """chekcing if City have attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """Tests if City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

        @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_City(self):
        """test if the save method is working"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """This tests if dictionary is working"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
