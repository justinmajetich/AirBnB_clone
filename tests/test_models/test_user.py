#!/usr/bin/python3
""" unittest for user class"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest

class test_User(unittest.TestCase,test_basemodel):
    """ class for user tests"""

    def __init__(self, *args, **kwargs):
        """ initialize the test"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ test first_name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """test last_name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """test email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test password """
        new = self.value()
        self.assertEqual(type(new.password), str)
