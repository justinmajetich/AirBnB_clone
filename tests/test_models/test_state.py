#!/usr/bin/python3
"""
    test state
"""
from models.base_model import BaseModel
from models.state import State
import unittest


class test_State(unittest.TestCase):
    """
        test for state class
    """
    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.dummy_state = State()
        cls.dummy_state.name = "tests"

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.dummy_state

    def test_inheritance(self):
        """
            test proper inheritance
        """
        self.assertIsInstance(self.dummy_state, BaseModel)
        self.assertTrue(hasattr(self.dummy_state, "id"))
        self.assertTrue(hasattr(self.dummy_state, "created_at"))
        self.assertTrue(hasattr(self.dummy_state, "updated_at"))

    def test_attrs(self):
        """
            test attributes
        """
        self.assertTrue(hasattr(self.dummy_state, "name"))

if __name__ == "__main__":
    unittest.main()
