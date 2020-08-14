#!/usr/bin/python3

import unittest
import os
import pep8
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_user = User()
        cls.my_user.first_name = "Betty"
        cls.my_user.last_name = "Holberton"
        cls.my_user.email = "airbnb@holbertonshool.com"
        cls.my_user.password = "root"

    @classmethod
    def tearDownClass(cls):
        del cls.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('id' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.first_name), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "testing skip")
    def test_save(self):
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.my_user), True)


if __name__ == "__main__":
    unittest.main()
