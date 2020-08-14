#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
from os import getenv


class test_City(test_basemodel):
    """ """

    if getenv("HBNB_TYPE_STORAGE") != "db":

        def __init__(self, *args, **kwargs):
            """ """
            super().__init__(*args, **kwargs)
            self.name = "City"
            self.value = City

        def test_state_id(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.state_id), str)

        def test_name(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.name), str)
    else:
        def test_state_id(self):
            """ """
            state = State(name="California")
            new = City(name="San Jose", state_id=state.id)
            self.assertEqual(type(new.state_id), str)

        def test_name(self):
            """ """
            state = State(name="California")
            new = City(name="San Jose", state_id=state.id)
            self.assertEqual(type(new.name), str)
