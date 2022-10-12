#!/usr/bin/python3
""" Unittest test cases for 'models.amenity' """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest


class test_Amenity(test_basemodel):
    """ Test the instantiation of the Amenity class. """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.model = Amenity

    def test_instance_exists(self):
        """ """
        self.assertIsNotNone(self.model)

    def test_class_attributes(self):
        """ """
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_class_attributes_type(self):
        """ """
        self.assertIsInstance(getattr(Amenity, 'name'), str)


if __name__ == '__main__':
    unittest.main()
