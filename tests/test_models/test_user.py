#!/usr/bin/python3
"""Test for User """
import os
import unittest
import pep8
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Tests for the class User that inherites from BaseModel"""

    def __init__(self, *args, **kwargs):
        """this initializes th test process"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @classmethod
    def setUpClass(cls):
        """This sets up for test"""
        cls.user = User()
        cls.user.first_name = "Kevin"
        cls.user.last_name = "Yook"
        cls.user.email = "yook00627@gmamil.com"
        cls.user.password = "secret"

    @classmethod
    def teardown(cls):
        """At the end of the test, this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown setup"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_User(self):
        """Tests for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_User(self):
        """his tests for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes_User(self):
        """Tests the User class has the expected attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass_User(self):
        """test if User is subclass of Basemodel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_first_name(self):
        """Test first_name attribute functinality of class User"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test last_name attribute functinality of class User"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Checks if the email attribute is set properly"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test that attribute of class User created by Value() works"""
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_save_User(self):
        """Tests if the save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_User(self):
        """Test if dictionary is working"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
