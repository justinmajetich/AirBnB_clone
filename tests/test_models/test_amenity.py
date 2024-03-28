#!/usr/bin/python3
""" Unittests for amenity class """
import unittest
from os import getenv
from datetime import datetime
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel


class test_Amenity(unittest.TestCase):
    """ Test class amenity"""

    def test_instantiation(self, *args, **kwargs):
        """ Test the amenity instantiation"""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, Amenity)
        self.assertIsNotNone(new_amenity.id)
        self.assertIsInstance(new_amenity.created_at, datetime)
        self.assertIsInstance(new_amenity.updated_at, datetime)     

    def test_attributes(self):
        """ Test amenities attributes """
        new_amenity = Amenity()
        new_amenity.name = "Spa"
        self.assertEqual(new_amenity.name, "Spa")
        
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            self.assertIsInstance(new_amenity.place_amenities, list)


if __name__ == '__main__':
    unittest.main()
