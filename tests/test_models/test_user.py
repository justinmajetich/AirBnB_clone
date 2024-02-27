#!/usr/bin/python3
""" test module for user class"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest
import pep8
import models.user


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


class TestUserDoc(unittest.TestCase):
    """Tests for documentation in user class"""

    def test_module_doc(self):
        """ checks for module doc"""
        self.assertGreaterEqual(len(models.user.__doc__), 1)

    def test_class_doc(self):
        """ checks for class doc"""
        self.assertGreaterEqual(len(User.__doc__), 1)


class TestUserpep8(unittest.TestCase):
    """ tests user class for pep8 compliance"""

    def test_pep8_compliance(self):
        """ test to ensure models/user.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """ test to ensure tests/test_models/test_user.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_user.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")