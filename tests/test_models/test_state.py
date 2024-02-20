#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.state import State
import unittest
import os
import pep8


class TestState(unittest.TestCase):
    """Tests the State class"""

    @classmethod
    def setUpClass(cls):
        """Creates a state instance"""

        cls.state = State()
        cls.state.name = 'Cairo'

    @classmethod
    def tearDownClass(cls):
        """Delete the state instance"""

        del cls.state

    def tearDown(self):
        """Removes file.json"""

        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attribute_existence(self):
        """Tests for attribute existence in State class"""

        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_attribute_type(self):
        """Tests type of attribute"""

        self.assertEqual(type(self.state.name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db',
                     'Database storage is being used')
    def test_save(self):
        """Tests save method"""

        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """tests to_dict method"""

        dict = self.state.to_dict()

        self.assertIsInstance(dict['created_at'], str)
        self.assertIsInstance(dict['updated_at'], str)
        self.assertEqual('to_dict' in dir(self.state), True)

    def test_issubclass(self):
        """Tests if State is subclass of Basemodel"""

        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_documentation(self):
        """Tests if the class is documented"""

        self.assertIsNotNone(State.__doc__)

    def test_following_pep8(self):
        """Tests if the code follows pep8 style guide"""

        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/state.py'])

        self.assertEqual(result.total_errors, 0, 'Found style errors.')


if __name__ == "__main__":
    unittest.main()
