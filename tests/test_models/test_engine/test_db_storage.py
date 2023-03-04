#!/usr/bin/python3
"""db storage tests"""
import unittest
from models.user import User


class TestUserModel(unittest.TestCase):
    """unittests"""
    def test_init(self):
        self.assertEqual(User, type(User()))


if __name__ == "__main__":
    unittest.main()
