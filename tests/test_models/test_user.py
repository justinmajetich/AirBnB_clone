#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Test for the class User"""

    def __init__(self, *args, **kwargs):
        """ Initialization of the test user"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ A test to check for the first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ A test to check for the last name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ A test to check for the email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ A test to check for the password"""
        new = self.value()
        self.assertEqual(type(new.password), str)
