#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.city import City
import unittest
import os
import pep8


class TestCity(unittest.TestCase):
    """Tests the City class"""

    @classmethod
    def setUpClass(cls):
        """Creates a city instance"""

        cls.city = City()
        cls.city.name = 'Heliopolis'
        cls.city.state_id = "654gdfsd"

    @classmethod
    def tearDownClass(cls):
        """Delete the city instance"""

        del cls.city

    def tearDown(self):
        """Removes file.json"""

        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attribute_existence(self):
        """Tests for attribute existence in City class"""

        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)

    def test_attribute_type(self):
        """Tests type of attribute"""

        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db',
                     'Database storage is being used')
    def test_save(self):
        """Tests save method"""

        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """tests to_dict method"""

        dict = self.city.to_dict()

        self.assertIsInstance(dict['created_at'], str)
        self.assertIsInstance(dict['updated_at'], str)
        self.assertEqual('to_dict' in dir(self.city), True)

    def test_issubclass(self):
        """Tests if City is subclass of Basemodel"""

        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_documentation(self):
        """Tests if the class is documented"""

        self.assertIsNotNone(City.__doc__)

    def test_following_pep8(self):
        """Tests if the code follows pep8 style guide"""

        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/city.py'])

        self.assertEqual(result.total_errors, 0, 'Found style errors.')


if __name__ == "__main__":
    unittest.main()
