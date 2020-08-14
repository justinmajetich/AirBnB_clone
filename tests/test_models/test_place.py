#!/usr/bin/python3

import unittest
import os
import pep8
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.place1 = Place()
        cls.place1.city_id = "Somewhere in India"
        cls.place1.user_id = "Aladdin"
        cls.place1.name = "Taj Mahal"
        cls.place1.description = "Fit for a king"
        cls.place1.number_rooms = 0
        cls.place1.number_bathrooms = 0
        cls.place1.max_guest = 0
        cls.place1.price_by_night = 0
        cls.place1.latitude = 0.0
        cls.place1.longitude = 0.0
        cls.place1.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        del cls.place1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.place1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Place.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.place1.__dict__)
        self.assertTrue('created_at' in self.place1.__dict__)
        self.assertTrue('updated_at' in self.place1.__dict__)
        self.assertTrue('city_id' in self.place1.__dict__)
        self.assertTrue('user_id' in self.place1.__dict__)
        self.assertTrue('name' in self.place1.__dict__)
        self.assertTrue('description' in self.place1.__dict__)
        self.assertTrue('number_rooms' in self.place1.__dict__)
        self.assertTrue('number_bathrooms' in self.place1.__dict__)
        self.assertTrue('max_guest' in self.place1.__dict__)
        self.assertTrue('price_by_night' in self.place1.__dict__)
        self.assertTrue('latitude' in self.place1.__dict__)
        self.assertTrue('longitude' in self.place1.__dict__)
        self.assertTrue('amenity_ids' in self.place1.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.place1.city_id), str)
        self.assertEqual(type(self.place1.user_id), str)
        self.assertEqual(type(self.place1.name), str)
        self.assertEqual(type(self.place1.description), str)
        self.assertEqual(type(self.place1.number_rooms), int)
        self.assertEqual(type(self.place1.number_bathrooms), int)
        self.assertEqual(type(self.place1.max_guest), int)
        self.assertEqual(type(self.place1.price_by_night), int)
        self.assertEqual(type(self.place1.latitude), float)
        self.assertEqual(type(self.place1.longitude), float)
        self.assertEqual(type(self.place1.amenity_ids), list)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
    def test_save(self):
        self.place1.save()
        self.assertNotEqual(self.place1.created_at, self.place1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.place1), True)


if __name__ == "__main__":
    unittest.main()
