#!/usr/bin/python3
"""Test State Class"""
import pycodestyle
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestStateDoc(unittest.TestCase):
    """check State documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(State.__doc__) > 0)


class TestStatePycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycodestyle(self):
        """tests pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/base_model.py']).total_errors,
            0, "PEP 8 style issues found"
        )


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """Test State Constructor"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test correct name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_state_inheritance(self):
        """test attributes of state class"""
        self.assertTrue(issubclass(self.value, BaseModel))


if __name__ == "__main__":
    unittest.main()
