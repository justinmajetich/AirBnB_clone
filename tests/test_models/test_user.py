#!/usr/bin/python3
"""Test module to test the User class using unittest moduel """
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class test_User(TestBaseModel):
    """ Subclass of the unittest class to test the User class"""

    def __init__(self, *args, **kwargs):
        """ Init the test class and its super"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Test the first_name attribute"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Tets the last_name attribute"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Test the email attribute"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Test the password attribute"""
        new = self.value()
        self.assertEqual(type(new.password), str)
