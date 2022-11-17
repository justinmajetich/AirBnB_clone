#!/usr/bin/python3
"""Test module for user class"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest
import pep8
import models.user


class test_User(test_basemodel):
    """Tests creation of User"""

    def __init__(self, *args, **kwargs):
        """Instantiates user for testing"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Tests proper creation of first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Tests proper creation of last name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Tests proper creation of email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Tests proper creation of email"""
        new = self.value()
        self.assertEqual(type(new.password), str)


class TestUserDoc(unittest.TestCase):
    """Tests for documentation in user class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.user.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(User.__doc__), 1)


class TestUserPep8(unittest.TestCase):
    """Tests User Class for pep8 compliance"""
    def test_pep8_compliance(self):
        """Tests to ensure models/user.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Tests that tests/test_models/test_user.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_user.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
