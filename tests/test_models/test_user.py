#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest


class test_User(test_basemodel):
    """ """
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.obj = User()
        cls.obj.first_name = "Charlie"
        cls.obj.last_name = "Lars"
        cls.obj.email = "test@mail.com"
        cls.obj.password = "GREGE643"

    def is_subclass(self):
        """ tests subclass of BaseModel """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)

    def test_first_name(self):
        """ """

        self.assertEqual(type(self.obj.first_name), str)

    def test_last_name(self):
        """ """
        self.assertEqual(type(self.obj.last_name), str)

    def test_email(self):
        """ """
        self.assertEqual(type(self.obj.email), str)

    def test_password(self):
        """ """
        self.assertEqual(type(self.obj.password), str)


if __name__ == "__main__":
    unittest.main()
