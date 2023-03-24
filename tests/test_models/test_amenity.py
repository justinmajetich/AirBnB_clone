#!/usr/bin/python3
"""Test for Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, None)


if __name__ == '__main__':
    unittest.main()
