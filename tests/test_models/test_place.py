#!/usr/bin/python3
"""
Test for Place class.
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for Place class.
    """

    def test_attributes(self):
        """
        Test Place attributes.
        """
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(place.city_id, None)
        self.assertEqual(place.user_id, None)
        self.assertEqual(place.name, None)
        self.assertEqual(place.description, None)
        self.assertEqual(place.number_rooms, None)
        self.assertEqual(place.number_bathrooms, None)
        self.assertEqual(place.max_guest, None)
        self.assertEqual(place.price_by_night, None)
        self.assertEqual(place.latitude, None)
        self.assertEqual(place.longitude, None)
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
