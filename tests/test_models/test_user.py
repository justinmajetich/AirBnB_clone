#!/usr/bin/python3
""" Unittest test cases for 'models.user' """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest


class TestUser_Instantiation(test_basemodel):
    """ Test the instantiation of the User class. """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.model = User

    def test_instance_exists(self):
        """ """
        self.assertIsNotNone(self.model)

    def test_class_attributes(self):
        """ """
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_class_attributes_type(self):
        """ """
        self.assertIsInstance(getattr(User, 'email'), str)
        self.assertIsInstance(getattr(User, 'password'), str)
        self.assertIsInstance(getattr(User, 'first_name'), str)
        self.assertIsInstance(getattr(User, 'last_name'), str)


if __name__ == '__main__':
    unittest.main()
