#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
import os
from models.base_model import BaseModel

type_storage = os.getenv('HBNB_TYPE_STORAGE')


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class test_statev2(unittest.TestCase):
    """ Class test state"""

    def test001(self):
        """Check if State is child of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test002(self):
        """ Check State default attributes """
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))
        self.assertTrue(state.name is "")

    def test003(self):
        """ Check State when type storage is db"""
        state = State()
        if (type_storage == 'db'):
            self.assertTrue(state.name is None)
