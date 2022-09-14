#!/usr/bin/python3
"""test state"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """class"""

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
