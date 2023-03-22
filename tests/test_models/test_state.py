#!/usr/bin/python3

import unittest
import os

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.state1 = State()
        cls.state1.name = "CA_the_golden_state"

    @classmethod
    def tearDownClass(cls):
        del cls.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.state1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('updated_at' in self.state1.__dict__)
        self.assertTrue('name' in self.state1.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.state1.name), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
    def test_save(self):
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.state1), True)


if __name__ == "__main__":
    unittest.main()
