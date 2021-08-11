#!/usr/bin/python3
""" Modules for tests amenity """
from models.amenity import Amenity
from models.base_model import BaseModel
import os
import unittest


class test_Amenity(unittest.TestCase):
    """ Tests for amenity """

    @classmethod
    def setUpClass(cls):
        """ set up for test """
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """ at the end of the test this will tear it down """
        del cls.amenity

    def test_checking_for_docstring_Amenity(self):
        """ checking for docstrings """
        self.assertIsNot(Amenity.__doc__, None)

    def test_is_subclass_Amenity(self):
        """ test if Amenity is subclass of Basemodel """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """ test attribute type for Amenity """
        self.assertEqual(type(self.amenity.name), str)

    def test_attributes_Amenity(self):
        """ chekcing if amenity have attributes """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        " This test only work in Filestorage ")
    def test_save_Amenity(self):
        """ test if the save works """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """ test if dictionary works """
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()