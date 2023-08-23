#!/usr/bin/python3
""" Test Amenity"""
import unittest
import os
from models.base_model import BaseModel
import pep8
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    @classmethod
    def setUpClass(cls):
        """test setup"""
        cls.amenity = Amenity()
        cls.amenity.name = "wifi"

    @classmethod
    def teardown(cls):
        """Test teardown"""
        del cls.amenity

    def tearDown(self):
        """teardown method"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/amenity.py'])
        self.assertEqual(res.total_errors, 0, "fix pep8")

    def test_docstring_Amenity(self):
        """checking for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_subclass(self):
        """test if Amenity is subclass of Basemodel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attributes(self):
        """chekcing amenity attibutes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_attribute_types(self):
        """test attribute type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def test_save(self):
        """test amenity save method"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        """test amenity to dict"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
