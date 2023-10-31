#!/usr/bin/python3
"""Tests for User class"""
import pycodestyle
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUserDoc(unittest.TestCase):
    """check User documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(User.__doc__) > 0)


class TestUserPycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycodestyle(self):
        """tests pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/user.py']).total_errors,
            0, "PEP 8 style issues found"
        )


class test_User(test_basemodel):
    """Tests for User class"""

    def __init__(self, *args, **kwargs):
        """Test User consructor"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test last name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """test email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test password"""
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_user_inheritance(self):
        """test attributes of user class"""
        self.assertTrue(issubclass(self.value, BaseModel))


if __name__ == "__main__":
    unittest.main()
