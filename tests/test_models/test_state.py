#!/usr/bin/env python3
"""
module to test the State class
"""
import unittest
import os
from models.state import State


class TestState(unittest.TestCase):
    """
    test state
    """

    def setUp(self):
        """setup"""
        if not os.path.exists("file.json"):
            os.mknod("file.json")
        self.state = State()

    def tearDown(self):
        """tear down"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        del self.state

    def test_creation(self):
        '''
        ensures correct creation
        '''
        self.assertEqual(self.state.name, '')

    def test_types(self):
        '''
        Test types
        '''
        self.assertEqual(type(self.state.name), str)

    def test_invalid_attributes(self):
        '''
        Test invalid attributes
        '''
        self.state = State({'first_name': 'Betty', 'last_name': 'Holberton'})
        self.assertFalse(hasattr(self.state, 'first_name'))
        self.assertFalse(hasattr(self.state, 'last_name'))
