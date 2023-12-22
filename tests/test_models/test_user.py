#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from unittest import skipIf
from os import getenv


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @skipIf(getenv("HBNB_TYPE_STORAGE") == 'db',
            "no test needed in db mode")
    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    @skipIf(getenv("HBNB_TYPE_STORAGE") == 'db',
            "no test needed in db mode")
    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    @skipIf(getenv("HBNB_TYPE_STORAGE") == 'db',
            "no test needed in db mode")
    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    @skipIf(getenv("HBNB_TYPE_STORAGE") == 'db',
            "no test needed in db mode")
    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_email_not_null(self):
        """ """
        new = User(email="hbnb@gmail.com", password="hbnbpwd")
        self.assertIsNotNone(new.email)

    def test_password_not_null(self):
        """ """
        new = User(email="hbnb@gmail.com", password="hbnbpwd")
        self.assertIsNotNone(new.password)
