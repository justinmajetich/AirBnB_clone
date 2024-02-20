#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
import os
import pep8


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Creates an amenity instance"""

        cls.amenity = Amenity()
        cls.amenity.name = 'Wifi'

    @classmethod
    def tearDownClass(cls):
        """Delete the amenity instance"""

        del cls.amenity

    def tearDown(self):
        """Removes file.json"""

        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attribute_existence(self):
        """Tests for attribute existence in Amenity class"""

        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_attribute_type(self):
        """Tests type of attribute"""

        self.assertEqual(type(self.amenity.name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db',
                     'Database storage is being used')
    def test_save(self):
        """Tests save method"""

        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        """tests to_dict method"""

        dict = self.amenity.to_dict()

        self.assertIsInstance(dict['created_at'], str)
        self.assertIsInstance(dict['updated_at'], str)
        self.assertEqual('to_dict' in dir(self.amenity), True)

    def test_issubclass(self):
        """Tests if Amenity is subclass of Basemodel"""

        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_documentation(self):
        """Tests if the class is documented"""

        self.assertIsNotNone(Amenity.__doc__)

    def test_following_pep8(self):
        """Tests if the code follows pep8 style guide"""

        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/amenity.py'])

        self.assertEqual(result.total_errors, 0, 'Found style errors.')


if __name__ == "__main__":
    unittest.main()
