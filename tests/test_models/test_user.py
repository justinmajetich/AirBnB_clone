#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from tests.test_models import storage_type


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ initize attributes """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ test first name attribute """
        new = self.value()
        self.assertEqual(type(new.first_name),
                         str if storage_type != "db" else type(None))

    def test_last_name(self):
        """ test last name attribute """
        new = self.value()
        self.assertEqual(type(new.last_name),
                         str if storage_type != "db" else type(None))

    def test_email(self):
        """ test email attribute """
        new = self.value()
        self.assertEqual(type(new.email),
                         str if storage_type != "db" else type(None))

    def test_password(self):
        """ test password attribute """
        new = self.value()
        self.assertEqual(type(new.password),
                         str if storage_type != "db" else type(None))
