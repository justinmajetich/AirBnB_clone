#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_email(self):
        # Create a new instance of the User model
        new_user = User(email='test@example.com', other_attribute='value')

        # Access the email attribute and check its type
        self.assertEqual(type(new_user.email), str)

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = User(password="password")
        self.assertEqual(type(new.password), str)

    def test_first_name(self):
        # Create a new instance of the User model
        new_user = User(first_name='John', other_attribute='value')

        # Access the first_name attribute and check its type
        self.assertEqual(type(new_user.first_name), str)


if __name__ == '__main__':
    unittest.main()
