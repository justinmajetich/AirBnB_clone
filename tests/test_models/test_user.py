#!/usr/bin/python3
"""User Class Test Cases"""
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_init(self):
        self.assertEqual(User, type(User()))

    def test_attributes(self):
        """Testing attributes"""
        usr = User(email="a", password="a")
        self.assertEqual(str, type(usr.id))
        self.assertTrue(hasattr, (usr, "__tablename__"))
        self.assertTrue(hasattr, (usr, "email"))
        self.assertTrue(hasattr, (usr, "password"))
        self.assertTrue(hasattr, (usr, "first_name"))
        self.assertTrue(hasattr, (usr, "last_name"))
        self.assertTrue(hasattr, (usr, "places"))
        self.assertTrue(hasattr, (usr, "reviews"))

    def test_first_name(self):
        """Testing type of first_name"""
        User.first_name = "Betty"
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        """Testing type of last_name"""
        User.last_name = "Holberton"
        self.assertEqual(str, type(User.last_name))


if __name__ == "__main__":
    unittest.main()