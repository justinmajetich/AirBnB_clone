#!/usr/bin/python3
""" Test """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Test """

    def __init__(self, *args, **kwargs):
        """ Test instantiation """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name_is_public_str(self):
        """ Testing first name """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name_is_public_str(self):
        """ Testing last name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email_is_public_str(self):
        """ Testing email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password_is_public_str(self):
        """ Testing password"""
        new = self.value()
        self.assertEqual(type(new.password), str)
