#!/usr/bin/python3
""" Unittest test cases for 'models.state' """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest


class test_state(test_basemodel):
    """ Test the instantiation of the State class. """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.model = State

    def test_instance_exists(self):
        """ """
        self.assertIsNotNone(self.model)

    def test_class_attributes(self):
        """ """
        self.assertTrue(hasattr(State, 'name'))

    def test_class_attributes_type(self):
        """ """
        self.assertIsInstance(getattr(State, 'name'), str)


if __name__ == '__main__':
    unittest.main()
