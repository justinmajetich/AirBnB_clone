#!/usr/bin/python3
""" """
import os
import unittest
import pep8
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User class"""

    @classmethod
    def setUpClass(cls):
        """Test set up"""
        cls.user = User()
        cls.user.first_name = "Yan"
        cls.user.last_name = "Tim"
        cls.user.email = "yan@email.com"
        cls.user.password = "yanpwd"

    @classmethod
    def teardown(cls):
        """Test tear down"""
        del cls.user

    def tearDown(self):
        """Teardown method"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pep8(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/user.py'])
        self.assertEqual(res.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Checking class docstring"""
        self.assertIsNotNone(User.__doc__)

    def test_subclass(self):
        """Test if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attributes(self):
        """Checking class attributes"""
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_attribute_types(self):
        """Test user attributes Types"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_save(self):
        """Test user save method"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """Test user to_dict method"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == '__main__':
    unittest.main()
