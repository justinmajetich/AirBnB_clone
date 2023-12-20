#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertIsNone(new.first_name)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertIsNone(new.last_name)

    def test_email(self):
        """ """
        new = self.value()
        self.assertIsNone(new.email)

    def test_password(self):
        """ """
        new = self.value()
        self.assertIsNone(new.password)
