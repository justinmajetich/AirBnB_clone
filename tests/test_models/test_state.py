#!/usr/bin/python3
""" Test for state """

import unittest
import models
from models.state import State
from models.base_model import BaseModel


class state_tests(unittest.TestCase):
    """ Tests for state file """

    def test_state(self):
        """ Test for the subclass state """
        instance = State()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_statename(self):
        """ Test the name """
        instance = State()
        self.assertTrue(hasattr(instance, "name"))
        self.assertEqual(instance.name, "")
