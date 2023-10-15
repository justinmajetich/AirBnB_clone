#!/usr/bin/python3
'''
    Contain tests for the state module.
'''
import unittest
from models.base_model import BaseModel
from models.state import State
from os import getenv, remove
import pep8

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestState(unittest.TestCase):
    '''
        Test the State class.
    '''

    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.new_state = State()
        cls.new_state.name = "California"

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.new_state
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_States_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_state.__tablename__, "states")

    def test_State_inheritence(self):
        '''
            Test that State class inherits from BaseModel.
        '''
        self.assertIsInstance(self.new_state, BaseModel)

    def test_State_attributes(self):
        '''
            Test that State class contains the attribute `name`.
        '''
        self.assertTrue("name" in self.new_state.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_State_attributes_type(self):
        '''
            Test that State class attribute name is class type str.
        '''
        name = getattr(self.new_state, "name")
        self.assertIsInstance(name, str)
