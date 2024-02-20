#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.user import User
import unittest
import os
import pep8


class TestUser(unittest.TestCase):
    """Tests the User class"""

    @classmethod
    def setUpClass(cls):
        """Creates a user instance"""

        cls.user = User()
        cls.user.email = 'example@m.com'
        cls.user.password = 'sa8d64f5g32'
        cls.user.first_name = 'Sebastian'
        cls.user.last_name = 'McCarthy'

    @classmethod
    def tearDownClass(cls):
        """Delete the user instance"""

        del cls.user

    def tearDown(self):
        """Removes file.json"""

        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attribute_existence(self):
        """Tests for attribute existence in user class"""

        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_attribute_type(self):
        """Tests type of attribute"""

        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db',
                     'Database storage is being used')
    def test_save(self):
        """Tests save method"""

        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """tests to_dict method"""

        dict = self.user.to_dict()

        self.assertIsInstance(dict['created_at'], str)
        self.assertIsInstance(dict['updated_at'], str)
        self.assertEqual('to_dict' in dir(self.user), True)

    def test_issubclass(self):
        """Tests if user is subclass of Basemodel"""

        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_documentation(self):
        """Tests if the class is documented"""

        self.assertIsNotNone(User.__doc__)

    def test_following_pep8(self):
        """Tests if the code follows pep8 style guide"""

        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/user.py'])

        self.assertEqual(result.total_errors, 0, 'Found style errors.')


if __name__ == "__main__":
    unittest.main()
