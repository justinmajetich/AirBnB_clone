#!/usr/bin/python3
""" """
import os
import unittest
import pep8
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test the Place class"""

    @classmethod
    def setUpClass(cls):
        """Test set up"""
        cls.place = Place()
        cls.place.city_id = "1234-abcd"
        cls.place.user_id = "5678-efgh"
        cls.place.name = "Studio"
        cls.place.description = "Huge room"
        cls.place.number_rooms = 1
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 3
        cls.place.price_by_night = 80
        cls.place.latitude = 1.6789
        cls.place.longitude = 1.2345
        cls.place.amenity_ids = ["1234-abcd"]

    @classmethod
    def teardown(cls):
        """Test tear down"""
        del cls.place

    def tearDown(self):
        """Teardown method"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pep8(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/place.py'])
        self.assertEqual(res.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Checking class docstring"""
        self.assertIsNotNone(Place.__doc__)

    def test_subclass(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_attributes(self):
        """Checking class attributes"""
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

    def test_attribute_types(self):
        """Test review attributes Types"""
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save(self):
        """Test Place save method"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict(self):
        """Test place to_dict method"""
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == '__main__':
    unittest.main()
