#!/usr/bin/python3
""" a module for user tests"""
import unittest
import pycodestyle
from models.user import User
import os


class TestUser(unittest.TestCase):
    """ a class for user tests"""

    @classmethod
    def setUpClass(cls):
        """ Example Data """
        cls.user = User()
        cls.user.first_name = "Madame"
        cls.user.last_name = "Tabitha"
        cls.user.email = "gildedlily@gmail.com"
        cls.user.password = "gildedlily123"

    @classmethod
    def teardown(cls):
        """ Tear down the class """
        del cls.user

    def tearDown(self):
        """ Tear down the file (file storage) """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pycodestyle_user(self):
        """tests for pycodestyle """
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(["models/user.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docs_user(self):
        """ check for docstrings """
        self.assertIsNotNone(User.__doc__)

    def test_attribute_types_User(self):
        """test attribute type for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)


if __name__ == "__main__":
    unittest.main()