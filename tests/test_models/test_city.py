#!/usr/bin/python3
""" """
import os
import unittest
from models.base_model import BaseModel
import pep8
from models.city import City


class TestCity(unittest.TestCase):
    """Test City class"""

    @classmethod
    def setUpClass(cls):
        """Test set up"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """test Tear down"""
        del cls.city

    def tearDown(self):
        """teardown method"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/city.py'])
        self.assertEqual(res.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """checking docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """chekcing City attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_subclass(self):
        """test if City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types(self):
        """test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_City(self):
        """test city save method"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """test city to_dict method"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
