#!/usr/bin/python3
"""This module tests the State class"""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """Tests the State class"""

    def test_state_name(self):
        """Tests the name attribute of the State class"""
        new = State(name="San Francisco")
        self.assertEqual(type(new.name), str)
