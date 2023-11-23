#!/usr/bin/python3
"""
module to test Place class
"""
import unittest
import os
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    test place
    """

    def setUp(self):
        """setup"""
        if not os.path.exists("file.json"):
            os.mknod("file.json")
        self.place = Place()

    def tearDown(self):
        """tear down"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        del self.place

    def test_creation(self):
        '''
        ensure correct initialization
        '''
        self.assertEqual(self.place.name, '')
        self.assertEqual(self.place.city_id, '')
        self.assertEqual(self.place.user_id, '')
        self.assertEqual(self.place.description, '')
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_types(self):
        '''
        Test types
        '''
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_invalid_attributes(self):
        '''
        Test invalid attributes
        '''
        self.place = Place({'location': 'San Francisco', 'owner': 'Betty'})
        self.assertFalse(hasattr(self.place, 'location'))
        self.assertFalse(hasattr(self.place, 'owner'))
