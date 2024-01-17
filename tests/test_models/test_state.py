#!/usr/bin/python3
""" testing state """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ test_state """

    def __init__(self, *args, **kwargs):
        """ __init__ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ test_name3 """
        new = self.value()
        self.assertEqual(type(new.name), str)
