#!/usr/bin/python3
"""
module to test Amenity class
"""
import unittest
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    test amenity
    """

    def setUp(self):
        """setUp"""
        if not os.path.exists("file.json"):
            os.mknod("file.json")
        self.amenity = Amenity()

    def tearDown(self):
        """tearDown"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        del self.amenity

    def test_creation(self):
        '''
        ensure correct creation
        '''
        self.assertEqual(self.amenity.name, '')

    def test_types(self):
        '''
        ensure types
        '''
        self.assertEqual(type(self.amenity.name), str)

    def test_invalid_attributes(self):
        '''
        Test invalid attributes
        '''
        self.amenity = Amenity({'first_name': 'Betty',
                                'last_name': 'Holberton'})
        self.assertFalse(hasattr(self.amenity, 'first_name'))
        self.assertFalse(hasattr(self.amenity, 'last_name'))
