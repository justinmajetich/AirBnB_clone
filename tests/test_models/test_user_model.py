#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.user import User
from io import StringIO
import sys
import datetime


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''

    def test_User_inheritance(self):
        '''
            tests that the User class Inherits from BaseModel
        '''
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_User_attributes(self):
        '''
            Test the user attributes exist
        '''

        new_user = User()
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())

    def test_type_email(self):
        '''
            Test the type of name
        '''
        new = User()
        name = getattr(new, "email")
        self.assertIsInstance(name, str)

    def test_type_first_name(self):
        '''
            Test the type of name
        '''
        new = User()
        name = getattr(new, "first_name")
        self.assertIsInstance(name, str)

    def test_type_last_name(self):
        '''
            Test the type of last_name
        '''
        new = User()
        name = getattr(new, "last_name")
        self.assertIsInstance(name, str)

    def test_type_password(self):
        '''
            Test the type of password
        '''
        new = User()
        name = getattr(new, "password")
        self.assertIsInstance(name, str)
