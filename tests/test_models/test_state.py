#!/usr/bin/python3
""" Test to State class"""
import models
from os import getenv
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from sqlalchemy.exc import OperationalError


class test_state(test_basemodel):
    """define state tests for State class"""

    def __init__(self, *args, **kwargs):
        """ Initialisation of State instance"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State
        self.state = State(name="California")

    def test_name3(self):
        """ test name in State instance"""
        self.assertEqual(type(self.state.name), str)
        self.assertEqual(self.state.name, "California")

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "not supported")
    def test_without_mandatory_arguments(self):
        """Check for mandatory arguments """
        new = self.value()
        with self.assertRaises(OperationalError):
            try:
                new.save()
            except Exception as error:
                models.storage._DBStorage__session.rollback()
                raise error

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "not supported")
    def test_is_subclass(self):
        """Check that State is a subclass of Basemodel"""
        self.assertTrue(isinstance(self.state, State))
