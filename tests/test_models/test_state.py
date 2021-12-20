#!/usr/bin/python3
""" Test for the State class"""
import models
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from sqlalchemy.exc import OperationalError


class test_state(test_basemodel):
    """ Defines State tests for State class """

    def __init__(self, *args, **kwargs):
        """ Initialisation of State instance """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State
        self.state = State(name="California")


    def test_name3(self):
        """ Test name of an State instance """
        new = self.value()
        self.assertEqual(type(self.state.name), str)
        self.assertEqual(self.state.name, "California")