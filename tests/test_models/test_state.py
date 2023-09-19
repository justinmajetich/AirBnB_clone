#!/usr/bin/python3
"""Test for the State"""
import os
import unittest
import pep8
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Tests for class State that inherites from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes the test case process"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @classmethod
    def setUpClass(cls):
        """This sets up for test"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def teardown(cls):
        """At the end of the test this will tear it down"""
        del cls.state

    def tearDown(self):
        """Teardown setup"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_State(self):
        """Test_check for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_name3(self):
        """Tests if the attribute type name3 of the class State works"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_save_State(self):
        """Tests if the save works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """Tests if dictionary is working"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
