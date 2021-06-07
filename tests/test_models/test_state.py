#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest

new = State(name='Idaho')


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        self.assertEqual(type(new.name), str)

"""    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") is None, "Using \
                     DBStorage")
    def test_cities(self):
        """ """
        self.assertEqual(type(new.cities), list)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE"), "Using \
                     FileStorage")
    def test_cities(self):
        """ """
        self.assertEqual(type(new.cities()), list)
"""
