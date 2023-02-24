#!/usr/bin/python3
"""
Tests for User
"""

import unittest
import pep8
from datetime import datetime
from io import StringIO
from contextlib import redirect_stdout
import models
from models.user import User


class TestUser(unittest.TestCase):
    """Test"""

    def setUp(self):
        self.user = User()

    def test_email(self):
        """
        1. test that the email attribute of the User object
           is an instance of the str class
        2. test that the email atttribute has the value of an empty string
        """
        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, "")

    def test_password(self):
        """
        1. test that the password attribute of the User object
           is an instance of the str class
        2. test that the password atttribute has the value of an empty string
        """
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password, "")

    def test_first_name(self):
        """
        1. test that the first_name attribute of the User object
           is an instance of the str class
        2. test that the first_name atttribute has the value of an empty string
        """
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, "")

    def test_last_name(self):
        """
        1. test that the last_name attribute of the User object
           is an instance of the str class
        2. test that the last_name atttribute has the value of an empty string
        """
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.last_name, "")

    def test_user_pep8(self):
        """test that user.py is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        """test that this file is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")


if __name__ == "__main__":
    unittest.main()
    