#!/usr/bin/python3
"""Defines the unittest for dbstrorage"""
import unittest
from models.engine.db_storage import DBStorage
from models.state import State


class TestDBStorage(unittest.TestCase):
    """This class tests the DBStorage class"""

    def setUp(self):
        """This method sets up the test environment"""
        self.storage = DBStorage()
        self.storage.reload()

    def tearDown(self):
        """This method tears down the test environment"""
        self.storage._DBStorage__session.close()

    def test_all(self):
        """This method tests the all method"""
        states = self.storage.all(State)
        self.assertIsInstance(states, dict)

    def test_new(self):
        """This method tests the new method"""
        state = State(name='California')
        self.storage.new(state)
        self.assertIn(state, self.storage._DBStorage__session)

    def test_save(self):
        """This method tests the save method"""
        state = State(name='California')
        self.storage.new(state)
        self.storage.save()
        self.assertIn(state, self.storage.all(State).values())

    def test_delete(self):
        """This method tests the delete method"""
        state = State(name='California')
        self.storage.new(state)
        self.storage.save()
        self.storage.delete(state)
        self.assertNotIn(state, self.storage.all(State).values())

    def test_reload(self):
        """This method tests the reload method"""
        state = State(name='California')
        self.storage.new(state)
        self.storage.save()
        self.storage.reload()
        self.assertNotIn(state, self.storage.all(State).values())
