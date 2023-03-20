#!/usr/bin/python3
"""test for city"""
import unittest
import os
from models.city import City
from models.state import State
from models.base_model import BaseModel
import pep8
from sqlalchemy import Column
from os import getenv


class TestCity(unittest.TestCase):
    """this will test the city class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.state = State()
        cls.state.name = "CA"
        cls.city.state_id = cls.state.id

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.city

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

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
        """test if City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "can't run if storage is db")
    def test_save_City(self):
        """test if the save works"""
        city = City()
        city.name = 'LA'
        state = State()
        state.name = 'CA'
        city.state_id = state.id
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

    def test_to_dict_City(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)

#    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
#    "can't run if storage is file")
#    def test_attributes_v2_City(self):
#        """Test the attributes in v2"""
#        self.assertTrue(self.city.__tablename__ == "cities")
#        self.assertTrue(type(self.city.name) == Column)
#        self.assertTrue(type(self.city.state_id) == Column)


if __name__ == "__main__":
    unittest.main()
