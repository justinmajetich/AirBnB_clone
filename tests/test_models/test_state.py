#!/usr/bin/python3
""" test module for state class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
import pep8
import models.state


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestStateDoc(unittest.TestCase):
    """Tests for documentation in state class"""

    def test_module_doc(self):
        """ checks for module doc"""
        self.assertGreaterEqual(len(models.state.__doc__), 1)

    def test_class_doc(self):
        """ checks for class doc"""
        self.assertGreaterEqual(len(State.__doc__), 1)


class TestReviewpep8(unittest.TestCase):
    """ tests state class for pep8 compliance"""

    def test_pep8_compliance(self):
        """ test to ensure models/state.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/state.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """ test to ensure tests/test_models/test_state.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_state.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")