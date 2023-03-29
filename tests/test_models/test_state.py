#!/usr/bin/python3
""" module for state reviews"""
import unittest
import pycodestyle
from models.state import State
from models.base_model import BaseModel
import os


class TestState(unittest.TestCase):
    """ a class for testing State"""

    @classmethod
    def setUpClass(cls):
        """ Example Data """
        cls.state = State()
        cls.state.name = "Covid-landia"

    def teardown(cls):
        """ tear down Class """
        del cls.state

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_pycodestyle_state(self):
        """check for pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(["models/state.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docs_state(self):
        """ check for docstring """
        self.assertIsNotNone(State.__doc__)

    def test_State_attribute_types(self):
        """ test State attribute types """
        self.assertEqual(type(self.state.name), str)

    def test_State_is_subclass(self):
        """ test if State is subclass of BaseModel """
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_State_save(self):
        """ test save() command """
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_State_sa_instance_state(self):
        """ test is _sa_instance_state has been removed """
        self.assertNotIn('_sa_instance_state', self.state.to_dict())


if __name__ == "__main__":
    unittest.main()