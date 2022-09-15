#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.user import User
from os import getenv, remove
from io import StringIO
import sys
import datetime
import pep8


storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''
    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.new_user = User()
        cls.new_user.email = "email@gmail.com"
        cls.new_user.password = "password"
        cls.new_user.firt_name = "Mel"
        cls.new_user.last_name = "Ng"

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.new_user
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_User_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_user.__tablename__, "users")

    def test_User_inheritance(self):
        '''
            tests that the User class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_user, BaseModel)

    def test_User_attributes(self):
        '''
            Test the user attributes exist
        '''
        self.assertTrue("email" in self.new_user.__dir__())
        self.assertTrue("first_name" in self.new_user.__dir__())
        self.assertTrue("last_name" in self.new_user.__dir__())
        self.assertTrue("password" in self.new_user.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_email(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_user, "email")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_first_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_user, "first_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_last_name(self):
        '''
            Test the type of last_name
        '''
        name = getattr(self.new_user, "last_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_password(self):
        '''
            Test the type of password
        '''
        name = getattr(self.new_user, "password")
        self.assertIsInstance(name, str)
