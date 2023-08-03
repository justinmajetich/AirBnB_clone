#!/usr/bin/python3
"""
test validation test state
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test case state"""

    def test_State_inheritence(self):
        """
        Test that State class inherits from BaseModel
        """
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        """
        Test that State class contains the attribute name
        """
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())
