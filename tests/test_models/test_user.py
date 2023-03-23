#!/usr/bin/python3
""" Unittest for class User"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Unittest for User class """

    def __init__(self, *args, **kwargs):
        """ test of initilisation class User"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ test of firstname type attribute"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ test of lastname type attribute"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ test of type email attribute """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """  test of password type attribute"""
        new = self.value()
        self.assertEqual(type(new.password), str)
