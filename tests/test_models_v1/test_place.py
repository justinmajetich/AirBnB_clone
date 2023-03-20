#!/usr/bin/env python3
"""
A unit test module for testing ``models/place.py`` module.
"""

import unittest
from models.place import Place
from datetime import datetime


class Test_Place(unittest.TestCase):
    """
    Test the basic features of the Place class.
    """

    def test_instance_uuid_is_unique(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = Place()
        user2 = Place()
        self.assertNotEqual(user1.id, user2.id)

    def test_instance_created_at_is_str(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = Place()
        self.assertEqual(type(user1.created_at), datetime)
        self.assertEqual(type(user1.updated_at), datetime)

    def test_save_method(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        from time import sleep
        user1 = Place()
        sleep(2)
        user1.save()
        self.assertNotEqual(user1.created_at, user1.updated_at)

    def test_string_representation(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = Place()
        string = "[{}] ({}) {}".format(user1.__class__.__name__,
                                       user1.id, user1.__dict__)
        self.assertEqual(user1.__str__(), string)

    def test_instance_dictionary(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = Place()
        user1.city_id = ""
        user1.user_id = ""
        user1.name = "betty"
        user1.description = ""
        user1.number_rooms = 0
        user1.number_bathrooms = 0
        user1.max_guest = 0
        user1.price_by_night = 0
        user1.latitude = 0.0
        user1.longitude = 0.0
        self.assertTrue("__class__" in user1.to_dict())
        self.assertTrue("city_id" in user1.to_dict())
        self.assertTrue("name" in user1.to_dict())
        self.assertTrue("user_id" in user1.to_dict())
        self.assertTrue("description" in user1.to_dict())
        self.assertTrue("number_rooms" in user1.to_dict())
        self.assertTrue("max_guest" in user1.to_dict())
        self.assertTrue("price_by_night" in user1.to_dict())
        self.assertTrue("latitude" in user1.to_dict())
        self.assertTrue("longitude" in user1.to_dict())

    def test_new_instance_from_dictionary(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = Place()
        model_json = user1.to_dict()
        user2 = Place(**model_json)
        self.assertFalse(user1 is user2)

    def test_new_instance_datetime_variables(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = Place()
        model_json = user1.to_dict()
        user2 = Place(**model_json)
        self.assertEqual(type(user2.created_at), datetime)
        self.assertEqual(type(user2.updated_at), datetime)

    def test_new_instance_properties_against_old(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = Place()
        user1.name = "New_Instance"
        model_json = user1.to_dict()
        user2 = Place(**model_json)
        self.assertEqual(type(user1), type(user2))
        self.assertEqual(user1.id, user2.id)
        self.assertEqual(user1.name, user2.name)
