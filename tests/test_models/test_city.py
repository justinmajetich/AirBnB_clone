#!/usr/bin/python3
""" """
from models.state import State
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """ Test for city"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        state = State()
        new = self.value()
        new.state_id = state.id
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        new.name = "Batch"
        self.assertEqual(type(new.name), str)
