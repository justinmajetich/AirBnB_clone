#!/usr/bin/python3
"""Defines unittests for user.py

Unittests classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of class: User"""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_new_gets_stored(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_public_and_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_public_and_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_public_and_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_and_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_and_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_and_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_and_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_ids_unique(self):
        usr1 = User()
        usr2 = User()
        self.assertNotEqual(usr1.id, usr2.id)

    def test_two_users_diff_created_at(self):
        usr1 = User()
        sleep(0.1)
        usr2 = User()
        self.assertLess(usr1.created_at, usr2.created_at)

    def test_two_users_diff_updated_at(self):
        usr1 = User()
        sleep(0.1)
        usr2 = User()
        self.assertLess(usr1.updated_at, usr2.updated_at)

    def test_str_value(self):
        d_t = datetime.now()
        d_t_r = repr(d_t)
        usr = User()
        usr.id = "66566"
        usr.created_at = d_t
        usr.updated_at = d_t
        usr_str = usr.__str__()
        self.assertIn("[User] (66566)", usr_str)
        self.assertIn("'id': '66566'", usr_str)
        self.assertIn("'created_at': " + d_t_r, usr_str)
        self.assertIn("'updated_at': " + d_t_r, usr_str)

    def test_arguments_not_used(self):
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def test_with_kwargs_None(self):
        with self.assertRaises(TypeError):
            User(id=None, create_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for save method of class: User"""

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", "other")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("other", "file.json")
        except IOError:
            pass

    def test_single_save(self):
        usr = User()
        sleep(0.1)
        first_update = usr.updated_at
        usr.save()
        self.assertLess(first_update, usr.updated_at)

    def test_two_saves(self):
        usr = User()
        sleep(0.1)
        first_update = usr.updated_at
        usr.save()
        second_update = usr.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.1)
        usr.save()
        self.assertLess(second_update, usr.updated_at)

    def test_save_with_argument(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)

    def test_save_updates_file(self):
        usr = User()
        usr.save()
        usr_id = "User." + usr.id
        with open("file.json", "r") as file:
            self.assertIn(usr_id, file.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of class: User"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_keys_accurate(self):
        usr = User()
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())

    def test_to_dict_containes_added_attr(self):
        usr = User()
        usr.middle_name = "Ryan"
        usr.meaning = 42
        self.assertEqual("Ryan", usr.middle_name)
        self.assertIn("meaning", usr.to_dict())

    def test_to_dict_datetime_is_str(self):
        usr = User()
        usr_dict = usr.to_dict()
        self.assertEqual(str, type(usr_dict["id"]))
        self.assertEqual(str, type(usr_dict["created_at"]))
        self.assertEqual(str, type(usr_dict["updated_at"]))

    def test_to_dict_out(self):
        d_t = datetime.now()
        usr = User()
        usr.id = "66566"
        usr.created_at = d_t
        usr.updated_at = d_t
        temp_dict = {
            'id': '66566',
            '__class__': 'User',
            'created_at': d_t.isoformat(),
            'updated_at': d_t.isoformat()
        }
        self.assertDictEqual(usr.to_dict(), temp_dict)

    def test_to_dict_dunder_dict_diff(self):
        usr = User()
        self.assertNotEqual(usr.to_dict(), usr.__dict__)

    def test_to_dict_with_argument(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.to_dict(None)


if __name__ == "__main__":
    unittest.main()
