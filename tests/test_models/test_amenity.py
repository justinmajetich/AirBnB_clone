#!/usr/bin/python3
""" module for state reviews"""
import unittest
import pycodestyle
from models.amenity import Amenity
from models.base_model import BaseModel
import os


class TestAmenity(unittest.TestCase):
    """ a class for testing Amenity"""

    @classmethod
    def setUpClass(cls):
        """ Example Data """
        cls.amen = Amenity()
        cls.amen.name = "Wifi"

    def teardown(cls):
        """ tear down Class """
        del cls.amen

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_Amenity_pycodestyle(self):
        """check for pycodestyle """
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(["models/amenity.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_Amenity_docs(self):
        """ check for docstring """
        self.assertIsNotNone(Amenity.__doc__)

    def test_Amenity_attribute_types(self):
        """ test Amenity attribute types """
        self.assertEqual(type(self.amen.name), str)

    def test_Amenity_is_subclass(self):
        """ test if Amenity is subclass of BaseModel """
        self.assertTrue(issubclass(self.amen.__class__, BaseModel), True)

    def test_Amenity_save(self):
        """ test save() command """
        self.amen.save()
        self.assertNotEqual(self.amen.created_at, self.amen.updated_at)

    def test_Amenity_sa_instance_state(self):
        """ test is _sa_instance_state has been removed """
        self.assertNotIn('_sa_instance_state', self.amen.to_dict())


if __name__ == "__main__":
    unittest.main()