#!/usr/bin/python3
""" """
import unittest
import os
from models.city import City
from models.base_model import BaseModel
import pep8


class test_City(test_basemodel):
    """Test for city """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8_City(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """checking for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """chekcing if City have attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "Test_DB")
    def test_save(self):
        """Test save"""
        self.city.save()
        self.assertFalse(self.city.created_at == self.city.updated_at)


if __name__ == "__main__":
    unittest.main()
