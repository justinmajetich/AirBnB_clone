#!/usr/bin/python3
""" """
import os
import unittest
from models.base_model import BaseModel
from models.state import State
import pep8


class TestState(unittest.TestCase):
    """Test State class"""

    @classmethod
    def setUpClass(cls):
        """Test set up"""
        cls.state = State()
        cls.state.name = "LA"

    @classmethod
    def teardown(cls):
        """Test teard down"""
        del cls.state

    def tearDown(self):
        """Teardown method"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pep8(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/state.py'])
        self.assertEqual(res.total_errors, 0, 'fix pep8')

    def test_docstring(self):
        """Checking docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_subclass(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attributes(self):
        """Checking State attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_attribute_types(self):
        """Test attributes types"""
        self.assertEqual(type(self.state.name), str)

    def test_save(self):
        """Test state save method"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """Test state o_dict method"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == '__main__':
    unittest.main()
