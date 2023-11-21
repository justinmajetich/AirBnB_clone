#!/usr/bin/python3
"""
import files
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """
    Test class for State model
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for test class
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        Test the 'name' attribute of State model
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
