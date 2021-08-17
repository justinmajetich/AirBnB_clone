#!/usr/bin/python3
""" """
import os
from unittest.case import skipIf
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_first_name(self):
        """ """
        new = self.value()
        new.first_name = "toto"
        self.assertIn("'first_name': '{}'".format(new.first_name), str(new))
        # self.assertEqual(type(new.first_name), str)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_last_name(self):
        """ """
        new = self.value()
        new.last_name = "George"
        self.assertIn("'last_name': '{}'".format(new.last_name), str(new))
        # self.assertEqual(type(new.last_name), str)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_email(self):
        """ """
        new = self.value()
        new.email = "test@test.com"
        self.assertIn("'email': '{}'".format(new.email), str(new))
        # self.assertEqual(type(new.email), str)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_password(self):
        """ """
        new = self.value()
        new.password = "test"
        self.assertIn("'password': '{}'".format(new.password), str(new))
        # self.assertEqual(type(new.password), str)
