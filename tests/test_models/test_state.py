#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from os import getenv


class test_state(test_basemodel):
    """ """

    if getenv("HBNB_TYPE_STORAGE") != "db":

        def __init__(self, *args, **kwargs):
            """ """
            super().__init__(*args, **kwargs)
            self.name = "State"
            self.value = State

        def test_name3(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.name), str)
    else:
        def test_name3(self):
            """ """
            new = State(name="Texas")
            self.assertEqual(type(new.name), str)
