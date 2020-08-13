#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os
from os import getenv


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
        self.user = self.value()
        self.user.first_name = "Andy"
        self.user.last_name = "Bay"
        self.user.email = "sono_va@gmamil.com"
        self.user.password = "simple123"

    def tearDown(self):
        """ removing file.json created and closing DB connection """
        if os.access("file.json", os.F_OK):
            os.remove("file.json")
        if getenv('HBNB_TYPE_STORAGE') == "db":
            try:
                self.db.close()
            except:
                pass

    def test_first_name(self):
        """ """
        self.assertEqual(type(self.user.first_name), str)

    def test_last_name(self):
        """ """
        self.assertEqual(type(self.user.last_name), str)

    def test_email(self):
        """ """
        self.assertEqual(type(self.user.email), str)

    def test_password(self):
        """ """
        self.assertEqual(type(self.user.password), str)
