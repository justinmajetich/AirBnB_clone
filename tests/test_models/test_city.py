#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
import os
import unittest

new = City(name='City_1', state_id=State(name='Oregon').id)


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(new.name), str)

"""    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") is None, "Using \
                     DBStorage")
    def test_places(self):
        """ """
        self.assertEqual(type(new.places), list)
"""
