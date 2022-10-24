#!/usr/bin/python3
"""Test module for state class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
import pep8
import models.state


class test_state(test_basemodel):
    """Tests State class"""

    def __init__(self, *args, **kwargs):
        """Instantiates state object"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Tests proper functionality of state name"""
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestStateDoc(unittest.TestCase):
    """Tests for documentation in state class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.state.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(State.__doc__), 1)


class TestStatePep8(unittest.TestCase):
    """Tests state Class for pep8 compliance"""

    def test_pep8_compliance(self):
        """Tests to ensure models/state.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/state.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Tests to ensure tests/test_models/test_state.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_state.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
