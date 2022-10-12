#!/usr/bin/python3
""" Unittest test cases for 'models.city' """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest


class test_City(test_basemodel):
    """ Test the instantiation of the City class. """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.model = City

    def test_instance_exists(self):
        """ """
        self.assertIsNotNone(self.model)

    def test_class_attributes(self):
        """ """
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'state_id'))

    def test_class_attributes_type(self):
        """ """
        self.assertIsInstance(getattr(City, 'name'), str)
        self.assertTrue(hasattr(City, 'state_id'))


if __name__ == '__main__':
    unittest.main()
