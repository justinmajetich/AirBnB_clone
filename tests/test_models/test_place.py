#!/usr/bin/python3
""" Tests place """

import unittest
import models
from models.place import Place
from models.base_model import BaseModel


class place_tests(unittest.TestCase):
    """ Tests for the place file"""

    def test_place(self):
        """Place is a subclass"""
        instance = Place()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_placename(self):
        """ Tests for the name """
        instance = Place()
        self.assertTrue(hasattr(instance, "city_id"))
        self.assertEqual(instance.city_id, "")
        self.assertTrue(hasattr(instance, "user_id"))
        self.assertEqual(instance.user_id, "")
        self.assertTrue(hasattr(instance, "name"))
        self.assertEqual(instance.name, "")
        self.assertTrue(hasattr(instance, "description"))
        self.assertEqual(instance.description, "")
        self.assertTrue(hasattr(instance, "number_rooms"))
        self.assertEqual(instance.number_rooms, 0)
        self.assertTrue(hasattr(instance, "number_bathrooms"))
        self.assertEqual(instance.number_bathrooms, 0)
        self.assertTrue(hasattr(instance, "max_guest"))
        self.assertEqual(instance.max_guest, 0)
        self.assertTrue(hasattr(instance, "price_by_night"))
        self.assertEqual(instance.price_by_night, 0)
        self.assertTrue(hasattr(instance, "latitude"))
        self.assertEqual(instance.price_by_night, 0.0)
        self.assertTrue(hasattr(instance, "longitude"))
        self.assertEqual(instance.longitude, 0.0)
