#!/usr/bin/python3
"""
This module defines extra tests for the State model
"""

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """
    Define test methods for the State model
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the class
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    '''
    # Test no longer required
    def test_name3(self):
        """
        Ensure that the attribute `name` of the class is a string
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
    '''
