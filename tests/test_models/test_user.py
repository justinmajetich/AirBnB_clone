#!/usr/bin/python3
""" Unittests for user class"""
import unittest
from models.user import User
from tests.test_models.test_base_model import test_basemodel


class test_User(test_basemodel):
    """ Test class for user"""

    def __init__(self, *args, **kwargs):
        """ Test User instantiation """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Test first name type """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Test last name type """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Test email type"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Test password type"""
        new = self.value()
        self.assertEqual(type(new.password), str)


if __name__ == '__main__':
    unittest.main()
