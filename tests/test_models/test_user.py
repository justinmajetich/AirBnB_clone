#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os

new = User(email="john69@hotmail.com", password="4201337",
           first_name="John", last_name="Hancock")


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        self.assertEqual(type(new.password), str)
