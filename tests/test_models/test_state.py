#!/usr/bin/python3
"""
    Test Case For state Model and its Test
"""
from models.base_model import BaseModel
from models.state import State
import unittest
import inspect
import time
from datetime import datetime
import pep8 as pcs
from unittest import mock
import models


class Teststate(unittest.TestCase):
    """
        unitesst for state class
    """

    def issub_class(self):
        """
            test if state class is sub class of base model
        """
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "update_at"))

    def test_name_attr(self):
        """
            Test that State has attribute name
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        if models.storage_type == "db":
            self.assertEqual(state.name, None)
        pass

    def test_to_dictstate(self):
        """
            test to dict method with state and the type
            and content
        """
        state = State()
        dict_cont = state.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in state.__dict__:
            self.assertTrue(attr in dict_cont)
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """
            test the returned dictionar values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        state = State()
        dict_con = state.to_dict()
        self.assertEqual(dict_con["__class__"], "State")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
            dict_con["created_at"],
            state.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_con["updated_at"],
            state.updated_at.strftime(time_format))
