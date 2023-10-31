#!/usr/bin/python3
""" """
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ This class tests the amenity class in models """

    @classmethod
    def setUpClass(cls):
        """ Set up test """
        cls.amenity = Amenity()
        cls.amenity.name = "Hot tub"

    @classmethod
    def tearDownClass(cls):
        """ Tears down class at the end of the testing """
        del cls.amenity

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attributes(self):
        """ Testing for amenity attributes """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_subcls(self):
        """ Testing if amenity is a sub class of basemodel """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attr_type(self):
        """ Testing for attribute types in amenity """
        self.assertEqual(type(self.amenity.name), str)

    def test_save(self):
        """ Test for save functionality """
        self.amenity.save
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

if __name__ == "__main__":
    unittest.main()