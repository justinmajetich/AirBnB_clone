#!/usr/bin/python3
"""
    test from basemodel
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
