#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from unittest.mock import patch
import pycodestyle
import models


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

    """test User"""

    def test_pep8_user(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_type_user(self):
        "test the type of attribute"
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)

    @classmethod
    def setup_class(self):
        """Setup for docstring"""
        self.user_1 = User()

    def test_docstrings(self):
        """test documentation"""
        self.assertIsNotNone(User.__doc__, "user.py needsa docstring")

    """Test if user inherit from BaseModel"""
    def test_instance(self):
        """check if user is an instance of BaseModel"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")

    """Testing user class"""
    @patch('models.user')
    def test_instances(self, mock_storage):
        instance = User()
        self.assertEqual(type(instance), User)
        instance.name = "OnePiece"
        instance.number = 981
        instance.email = "treasure@anime.com"
        instance.password = "smile"
        instance.first_name = "luffy"
        instance.last_name = "monkey"
        expectec_attrs_types = {
                "id": str,
                "created_at": datetime,
                "updated_at": datetime,
                "name": str,
                "number": int,
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
                }
        inst_dict = instance.to_dict()
        expected_dict_attrs = [
                "id",
                "created_at",
                "updated_at",
                "name",
                "number",
                "email",
                "password",
                "first_name",
                "last_name",
                "__class__"
                ]
        self.assertCountEqual(inst_dict.keys(), expected_dict_attrs)
        self.assertEqual(inst_dict['name'], 'OnePiece')
        self.assertEqual(inst_dict['number'], 981)
        self.assertEqual(inst_dict['email'], 'treasure@anime.com')
        self.assertEqual(inst_dict['password'], 'smile')
        self.assertEqual(inst_dict['first_name'], 'luffy')
        self.assertEqual(inst_dict['last_name'], 'monkey')
        self.assertEqual(inst_dict['__class__'], 'User')

        for attr, types in expectec_attrs_types.items():
            with self.subTest(attr=attr, typ=types):
                self.assertIn(attr, instance.__dict__)
                self.assertIs(type(instance.__dict__[attr]), types)
        self.assertEqual(instance.name, "OnePiece")
        self.assertEqual(instance.number, 981)
        self.assertEqual(instance.email, "treasure@anime.com")
        self.assertEqual(instance.first_name, "luffy")
        self.assertEqual(instance.last_name, "monkey")

    def test_user_id_and_createat(self):
        """testing id for every user"""
        user_1 = User()
        sleep(2)
        user_2 = User()
        sleep(2)
        user_3 = User()
        sleep(2)
        list_users = [user_1, user_2, user_3]
        for instance in list_users:
            user_id = instance.id
            with self.subTest(user_id=user_id):
                self.assertIs(type(user_id), str)
        self.assertNotEqual(user_1.id, user_2.id)
        self.assertNotEqual(user_1.id, user_3.id)
        self.assertNotEqual(user_2.id, user_3.id)
        self.assertTrue(user_1.created_at <= user_2.created_at)
        self.assertTrue(user_2.created_at <= user_3.created_at)
        self.assertNotEqual(user_1.created_at, user_2.created_at)
        self.assertNotEqual(user_1.created_at, user_3.created_at)
        self.assertNotEqual(user_3.created_at, user_2.created_at)

    def test_str_method(self):
        """
        Testin str magic method
        """
        inst = User()
        str_output = "[User] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(str_output, str(inst))

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Testing save method and if it update"""
        instance5 = User()
        created_at = instance5.created_at
        sleep(2)
        updated_at = instance5.updated_at
        instance5.save()
        new_created_at = instance5.created_at
        sleep(2)
        new_updated_at = instance5.updated_at
        self.assertNotEqual(updated_at, new_updated_at)
        self.assertEqual(created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)


if __name__ == '__main__':
    unittest.main()
