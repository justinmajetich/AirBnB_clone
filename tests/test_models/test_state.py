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
