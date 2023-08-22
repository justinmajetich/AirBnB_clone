#!/usr/bin/python3
"""Unittests for testing the User class """
import models
from os import getenv
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from sqlalchemy.exc import OperationalError


class test_User(test_basemodel):
    """Unittests for testing the User class"""

    def __init__(self, *args, **kwargs):
        """ Instantiation of User instance """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
        self.user = User(email="Erney@chocorramo.com", password="conleche")

    def test_first_name(self):
        """ test first name of user instance"""
        self.assertEqual(self.user.first_name, None)

    def test_last_name(self):
        """ test last name of user instance"""
        self.assertEqual(self.user.last_name, None)

    def test_email(self):
        """ test email of user instance"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(self.user.email, "Erney@chocorramo.com")

    def test_password(self):
        """ test if the password is string """
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(self.user.password, "conleche")

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "not supported")
    def test_without_mandatory_arguments(self):
        """Check for mandatory arguments """
        new = self.value()
        with self.assertRaises(OperationalError):
            try:
                new.save()
            except Exception as error:
                models.storage._DBStorage__session.rollback()
                raise error

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "not supported")
    def test_is_subclass(self):
        """Check that State is a subclass of Basemodel"""
        self.assertTrue(isinstance(self.user, User))
