#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.place import Place
import unittest
import os
import pep8


class TestPlace(unittest.TestCase):
    """Tests the Place class"""

    @classmethod
    def setUpClass(cls):
        """Creates a place instance"""

        cls.place = Place()
        cls.place.city_id = '5df1xghfc'
        cls.place.user_id = 'e65s4trgd'
        cls.place.name = 'Cozy House in The Forest'
        cls.place.description = 'A good place to relax'
        cls.place.number_rooms = 4
        cls.place.number_bathrooms = 5
        cls.place.max_guest = 20
        cls.place.price_by_night = 100
        cls.place.latitude = 30.03
        cls.place.longitude = 31.23
        cls.place.amenity_ids = ['68453asfd']

    @classmethod
    def tearDownClass(cls):
        """Delete the place instance"""

        del cls.place

    def tearDown(self):
        """Removes file.json"""

        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attribute_existence(self):
        """Tests for attribute existence in Place class"""

        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_attribute_type(self):
        """Tests type of attributes"""

        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db',
                     'Database storage is being used')
    def test_save(self):
        """Tests save method"""

        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict(self):
        """tests to_dict method"""

        dict = self.place.to_dict()

        self.assertIsInstance(dict['created_at'], str)
        self.assertIsInstance(dict['updated_at'], str)
        self.assertEqual('to_dict' in dir(self.place), True)

    def test_issubclass(self):
        """Tests if Place is subclass of Basemodel"""

        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_documentation(self):
        """Tests if the class is documented"""

        self.assertIsNotNone(Place.__doc__)

    def test_following_pep8(self):
        """Tests if the code follows pep8 style guide"""

        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/place.py'])

        self.assertEqual(result.total_errors, 0, 'Found style errors.')


if __name__ == "__main__":
    unittest.main()
