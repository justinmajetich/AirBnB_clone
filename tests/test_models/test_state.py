#!/usr/bin/python3
"""State Module Tests"""
import unittest
import models
import os
from datetime import datetime
from models.state import State
import sqlalchemy.orm


class TestStateModel(unittest.TestCase):
    def test_init(self):
        self.assertEqual(State, type(State()))

    def test_state_name(self):
        ok = State()
        self.assertEqual(sqlalchemy.orm.attributes.InstrumentedAttribute,
                         type(State.name))
        self.assertIn("name", dir(State()))
        self.assertNotIn("name", ok.__dict__)