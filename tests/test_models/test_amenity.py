#!/usr/bin/python3
"""test dor amenity """
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class test_Amenity(test_basemodel):
    """some test """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8_Amenity(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Amenity(self):
        """checking for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """chekcing if amenity have attibutes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "Test_DB")
    def test_save(self):
        """Test save"""
        self.amenity.save()
        self.assertFalse(self.amenity.created_at == self.amenity.updated_at)


if __name__ == "__main__":
    unittest.main()
