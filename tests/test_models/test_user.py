#!/usr/bin/python3
"""
script defines a test case (test_User) for the User class
"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """
    Test case for the User class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test case with the name "User" and the User class
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Test the 'first_name' attribute of a User object
        """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        Test the 'last_name' attribute of a User object
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        Test the 'email' attribute of a User object
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        Test the 'password' attribute of a User object
        """
        new = self.value()
        self.assertEqual(type(new.password), str)
