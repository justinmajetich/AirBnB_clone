#!/usr/bin/python3
"""
This module defines extra tests for the User model
"""

from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """
    Define extra tests for the User model
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the class
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Ensure that the `first_name` attribute is a string
        """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        Ensure that the `last_name` attribute is a string
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        Ensure that the `email` attribute is a string
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        Ensure that the `password` attribute is a string
        """
        new = self.value()
        self.assertEqual(type(new.password), str)
