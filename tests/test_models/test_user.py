#!/usr/bin/python3
""" Test for user"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """ This will test the User class """

    @classmethod
    def setUpClass(cls):
        """ Set up for test """
        cls.user = User()
        cls.user.first_name = "fouad"
        cls.user.last_name = "farid"
        cls.user.email = "devEAF@gmamil.com"
        cls.user.password = "secret"

    @classmethod
    def teardown(cls):
        """ At the end of the test this will tear it down """
        del cls.user

    def tearDown(self):
        """ Teardown """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_User(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_User(self):
        """ Checking for docstrings """
        self.assertIsNotNone(User.__doc__)

    def test_attributes_User(self):
        """ Chekcing if User have attributes """
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass_User(self):
        """ Test if User is subclass of Basemodel """
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types_User(self):
        """ Test attribute type for User """
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save_User(self):
        """ Test if the save works """
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_User(self):
        """ Test if dictionary works """
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
