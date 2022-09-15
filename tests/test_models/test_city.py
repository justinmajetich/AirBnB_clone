#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from os import getenv, remove

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
        cls.new_city = City()
        cls.new_city.state_id = "California"
        cls.new_city.name_id = "San Francisco"

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.new_city
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_City_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_city.__tablename__, "cities")

    def test_City_inheritance(self):
        '''
            Tests that the City class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_city, BaseModel)

    def test_User_attributes(self):
        '''
            Test user attributes exist
        '''
        self.assertTrue("state_id" in self.new_city.__dir__())
        self.assertTrue("name" in self.new_city.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_city, "name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_city, "state_id")
        self.assertIsInstance(name, str)
