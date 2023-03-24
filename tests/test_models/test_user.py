#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.user import User
from os import getenv

class test_User(TestBaseModel):
    """ """
    if getenv("HBNB_TYPE_STORAGE") != "db":
        def __init__(self, *args, **kwargs):
            """ """
            super().__init__(*args, **kwargs)
            self.name = "User"
            self.value = User

        def test_first_name(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.first_name), str)

        def test_last_name(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.last_name), str)

        def test_email(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.email), str)

        def test_password(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.password), str)
