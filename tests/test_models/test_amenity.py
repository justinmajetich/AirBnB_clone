#!/usr/bin/python3
""" Test for amenity """
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """ This will test the Amenity class """

    @classmethod
    def setUpClass(cls):
        """ Set up for test """
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """ At the end of the test this will tear it down """
        del cls.amenity

    def tearDown(self):
        """ Teardown """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Amenity(self):
        """ Test pep8 style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Amenity(self):
        """ Checking for docstring """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """ Chekcing if amenity have attibutes """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_Amenity(self):
        """ Test if Amenity is subclass of Basemodel """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """ Test attribute type for Amenity """
        self.assertEqual(type(self.amenity.name), str)

    def test_save_Amenity(self):
        """ Test if the save works """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """ Test if dictionary works """
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
