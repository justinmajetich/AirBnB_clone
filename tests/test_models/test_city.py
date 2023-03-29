#!/usr/bin/python3
""" module for state reviews"""
import unittest
import pycodestyle
from models.city import City
from models.base_model import BaseModel
import os


class TestCity(unittest.TestCase):
    """ a class for testing City"""

    @classmethod
    def setUpClass(cls):
        """ Example Data """
        cls.city = City()
        cls.city.name = "San Francisco"
        cls.city.state_id = "san-francisco"

    def teardown(cls):
        """ tear down Class """
        del cls.city

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_City_pycodestyle(self):
        """check for pycodestyle """
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(["models/city.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_City_docs(self):
        """ check for docstring """
        self.assertIsNotNone(City.__doc__)

    def test_City_attribute_types(self):
        """ test City attribute types """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_City_is_subclass(self):
        """ test if City is subclass of BaseModel """
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "City won't save\
                     because it needs to be tied to a state :\\")
    def test_City_save(self):
        """ test save() command """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_City_sa_instance_state(self):
        """ test is _sa_instance_state has been removed """
        self.assertNotIn('_sa_instance_state', self.city.to_dict())


if __name__ == "__main__":
    unittest.main()