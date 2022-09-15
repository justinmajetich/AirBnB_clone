#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.place import Place
from os import getenv, remove

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestPlace(unittest.TestCase):
    '''
        Testing Place class
    def test_pep8_style_check(self):
            Tests pep8 style
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/places.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error needs fixing")

    '''

    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.new_place = Place(city_id="0O01", user_id="0O02", name="house",
                              description="awesome", number_rooms=3,
                              number_bathrooms=2, max_guest=1,
                              price_by_night=100, latitude=37.77,
                              longitude=127.12)

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.new_place
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_Place_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_place.__tablename__, "places")

    def test_Place_inheritance(self):
        '''
            tests that the City class Inherits from BaseModel
        '''

        self.assertIsInstance(self.new_place, BaseModel)

    def test_Place_attributes(self):
        '''
            Checks that the attribute exist.
        '''
        self.assertTrue("city_id" in self.new_place.__dir__())
        self.assertTrue("user_id" in self.new_place.__dir__())
        self.assertTrue("description" in self.new_place.__dir__())
        self.assertTrue("name" in self.new_place.__dir__())
        self.assertTrue("number_rooms" in self.new_place.__dir__())
        self.assertTrue("max_guest" in self.new_place.__dir__())
        self.assertTrue("price_by_night" in self.new_place.__dir__())
        self.assertTrue("latitude" in self.new_place.__dir__())
        self.assertTrue("longitude" in self.new_place.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_place_amenity_attrb(self):
        self.assertTrue("amenity_ids" in self.new_place.__dir__())

    @unittest.skipIf(storage != "db", "Testing database storage only")
    def test_place_amenity_dbattrb(self):
        self.assertTrue("amenities" in self.new_place.__dir__())
        self.assertTrue("reviews" in self.new_place.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_longitude(self):
        '''
            Test the type of longitude.
        '''
        longitude = getattr(self.new_place, "longitude")
        self.assertIsInstance(longitude, float)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_latitude(self):
        '''
            Test the type of latitude
        '''
        latitude = getattr(self.new_place, "latitude")
        self.assertIsInstance(latitude, float)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_amenity(self):
        '''
            Test the type of latitude
        '''
        amenity = getattr(self.new_place, "amenity_ids")
        self.assertIsInstance(amenity, list)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_price_by_night(self):
        '''
            Test the type of price_by_night
        '''
        price_by_night = getattr(self.new_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_max_guest(self):
        '''
            Test the type of max_guest
        '''
        max_guest = getattr(self.new_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_number_bathrooms(self):
        '''
            Test the type of number_bathrooms
        '''
        number_bathrooms = getattr(self.new_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_number_rooms(self):
        '''
            Test the type of number_bathrooms
        '''
        number_rooms = getattr(self.new_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_description(self):
        '''
            Test the type of description
        '''
        description = getattr(self.new_place, "description")
        self.assertIsInstance(description, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_place, "name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_user_id(self):
        '''
            Test the type of user_id
        '''
        user_id = getattr(self.new_place, "user_id")
        self.assertIsInstance(user_id, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_city_id(self):
        '''
            Test the type of city_id
        '''
        city_id = getattr(self.new_place, "city_id")
        self.assertIsInstance(city_id, str)
