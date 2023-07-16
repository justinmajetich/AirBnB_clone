#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.state import State

class TestDBStorage(unittest.TestCase):

    def setUp(self):
        """Set up method for the test case"""
        self.storage = DBStorage()

    def tearDown(self):
        """Tear down method for the test case"""
        # Add necessary cleanup here

    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        # Add more assertions here based on your requirements

    def test_all_with_class(self):
        """Test that all returns only instances of a specific type when class is passed"""
        all_states = self.storage.all(State)
        self.assertIsInstance(all_states, dict)
        for obj_id, obj in all_states.items():
            self.assertIsInstance(obj, State)
        # Add more assertions here based on your requirements

    def test_new(self):
        """Test that new adds an object to the database"""
        state = State(name="New York")
        self.storage.new(state)
        self.storage.save()
        all_states = self.storage.all(State)
        self.assertIn(state.id, all_states)
        # Add more assertions here based on your requirements

    def test_delete(self):
        """Test that delete removes an object from the database"""
        state = State(name="New York")
        self.storage.new(state)
        self.storage.save()
        self.storage.delete(state)
        all_states = self.storage.all(State)
        self.assertNotIn(state.id, all_states)
        # Add more assertions here based on your requirements

    # Add more tests as needed for other methods and scenarios

if __name__ == "__main__":
    unittest.main()
