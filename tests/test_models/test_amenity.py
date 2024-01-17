#!/usr/bin/python3
"""
Test for Amenity class.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class.
    """

    def test_attributes(self):
        """
        Test Amenity attributes.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
