#!/usr/bin/python3
"""
    test amenities
"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class test_Amenity(unittest.TestCase):
    """
        test for amenity class
    """
    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.dummy_amenity = Amenity()
        cls.dummy_amenity.name = "test"

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.dummy_amenity

    def test_inheritance(self):
        """
            test proper inheritance
        """
        self.assertIsInstance(self.dummy_amenity, BaseModel)
        self.assertTrue(hasattr(self.dummy_amenity, "id"))
        self.assertTrue(hasattr(self.dummy_amenity, "created_at"))
        self.assertTrue(hasattr(self.dummy_amenity, "updated_at"))

    def test_attrs(self):
        """
            test attributes
        """
        self.assertTrue(hasattr(self.dummy_amenity, "name"))

if __name__ == "__main__":
    unittest.main()
