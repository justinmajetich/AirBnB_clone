#!/usr/bin/env python3
"""
module to test the City class
"""
import unittest
import os
from models.city import City


class TestCity(unittest.TestCase):
    """
    test city
    """

    def setUp(self):
        """setup"""
        if not os.path.exists("file.json"):
            os.mknod("file.json")
        self.city = City()

    def tearDown(self):
        """tear down"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        del self.city

    def test_creation(self):
        '''
        ensure correct creation
        '''
        self.assertEqual(self.city.name, '')
        self.assertEqual(self.city.state_id, '')

    def test_types(self):
        '''
        ensure types
        '''
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_invalid_attributes(self):
        '''
        Test invalid attributes
        '''
        self.city = City({'title': 'San Francisco', 'stateId': 'CA'})
        self.assertFalse(hasattr(self.city, 'stateId'))
        self.assertFalse(hasattr(self.city, 'title'))
