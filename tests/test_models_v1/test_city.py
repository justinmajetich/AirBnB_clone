#!/usr/bin/env python3
"""
A unit test module for testing ``models/city.py`` module.
"""

import unittest
from models.city import City
from datetime import datetime


class Test_City(unittest.TestCase):
    """
    Test the basic features of the City class.
    """

    def test_instance_uuid_is_unique(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = City()
        user2 = City()
        self.assertNotEqual(user1.id, user2.id)

    def test_instance_created_at_is_str(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = City()
        self.assertEqual(type(user1.created_at), datetime)
        self.assertEqual(type(user1.updated_at), datetime)

    def test_save_method(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        from time import sleep
        user1 = City()
        sleep(2)
        user1.save()
        self.assertNotEqual(user1.created_at, user1.updated_at)

    def test_string_representation(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = City()
        string = "[{}] ({}) {}".format(user1.__class__.__name__,
                                       user1.id, user1.__dict__)
        self.assertEqual(user1.__str__(), string)

    def test_instance_dictionary(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = City()
        user1.name = "New Instance variable"
        self.assertTrue("__class__" in user1.to_dict())
        self.assertTrue("name" in user1.to_dict())

    def test_new_instance_from_dictionary(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = City()
        model_json = user1.to_dict()
        user2 = City(**model_json)
        self.assertFalse(user1 is user2)

    def test_new_instance_datetime_variables(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = City()
        model_json = user1.to_dict()
        user2 = City(**model_json)
        self.assertEqual(type(user2.created_at), datetime)
        self.assertEqual(type(user2.updated_at), datetime)

    def test_new_instance_properties_against_old(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = City()
        user1.name = "New_Instance"
        user1.state_id = "new stateid"
        model_json = user1.to_dict()
        user2 = City(**model_json)
        self.assertEqual(type(user1), type(user2))
        self.assertEqual(user1.id, user2.id)
        self.assertEqual(user1.state_id, user2.state_id)
        self.assertEqual(user1.name, user2.name)
