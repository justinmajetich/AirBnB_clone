#!/usr/bin/env python3
"""
A unit test module for testing ``models/user.py`` module.
"""

import unittest
from models.user import User
from datetime import datetime


class Test_User(unittest.TestCase):
    """
    Test the basic features of the BaseModel class.
    """

    def test_instance_uuid_is_unique(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_instance_created_at_is_str(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = User()
        self.assertEqual(type(user1.created_at), datetime)
        self.assertEqual(type(user1.updated_at), datetime)

    def test_save_method(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        from time import sleep
        user1 = User()
        sleep(2)
        user1.save()
        self.assertNotEqual(user1.created_at, user1.updated_at)

    def test_string_representation(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = User()
        string = "[{}] ({}) {}".format(user1.__class__.__name__,
                                       user1.id, user1.__dict__)
        self.assertEqual(user1.__str__(), string)

    def test_instance_dictionary(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = User()
        user1.email = "uthman@gmail.com"
        user1.first_name = "uthman"
        user1.last_name = "betty"
        user1.password = "nothing"
        self.assertTrue("__class__" in user1.to_dict())
        self.assertTrue("email" in user1.to_dict())
        self.assertTrue("first_name" in user1.to_dict())
        self.assertTrue("last_name" in user1.to_dict())
        self.assertTrue("password" in user1.to_dict())

    def test_new_instance_from_dictionary(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = User()
        model_json = user1.to_dict()
        user2 = User(**model_json)
        self.assertFalse(user1 is user2)

    def test_new_instance_datetime_variables(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = User()
        model_json = user1.to_dict()
        user2 = User(**model_json)
        self.assertEqual(type(user2.created_at), datetime)
        self.assertEqual(type(user2.updated_at), datetime)

    def test_new_instance_properties_against_old(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        user1 = User()
        user1.name = "New_Instance"
        model_json = user1.to_dict()
        user2 = User(**model_json)
        self.assertEqual(type(user1), type(user2))
        self.assertEqual(user1.id, user2.id)
        self.assertEqual(user1.email, user2.email)
        self.assertEqual(user1.first_name, user2.first_name)
        self.assertEqual(user1.last_name, user2.last_name)
        self.assertEqual(user1.password, user2.password)
        self.assertEqual(user1.name, user2.name)
