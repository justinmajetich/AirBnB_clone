#!/usr/bin/python3
""" testing user """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """test_User """

    def __init__(self, *args, **kwargs):
        """ __init__ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ test_first_name """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ test_last_name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ test_email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        test_password """
        new = self.value()
        self.assertEqual(type(new.password), str)
