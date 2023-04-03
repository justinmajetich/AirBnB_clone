#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest


class test_state(test_basemodel):
    """ test State class """
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.obj = State()
        cls.obj.name = "Arizona"

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(self.obj.name), str)
    
    def is_subclass(self):
        """ tests subclass of BaseModel """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)


if __name__ == "__main__":
    unittest.main()
