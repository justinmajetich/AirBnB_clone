#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestUser(unittest.TestCase):
    '''
        Testing Place class
    '''

    def setUp(self):
        '''
            Creates an instance for place.
        '''
        self.new_place = Place()

    def TearDown(self):
        pass

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
        self.assertTrue("amenity_ids" in self.new_place.__dir__())

    def test_type_longitude(self):
        '''
            Test the type of longitude.
        '''
        longitude = getattr(self.new_place, "longitude")
        self.assertIsInstance(longitude, float)

    def test_type_latitude(self):
        '''
            Test the type of latitude
        '''
        latitude = getattr(self.new_place, "latitude")
        self.assertIsInstance(latitude, float)

    def test_type_amenity(self):
        '''
            Test the type of latitude
        '''
        amenity = getattr(self.new_place, "amenity_ids")
        self.assertIsInstance(amenity, list)

    def test_type_price_by_night(self):
        '''
            Test the type of price_by_night
        '''
        price_by_night = getattr(self.new_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    def test_type_max_guest(self):
        '''
            Test the type of max_guest
        '''
        max_guest = getattr(self.new_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    def test_type_number_bathrooms(self):
        '''
            Test the type of number_bathrooms
        '''
        number_bathrooms = getattr(self.new_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    def test_type_number_rooms(self):
        '''
            Test the type of number_bathrooms
        '''
        number_rooms = getattr(self.new_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    def test_type_description(self):
        '''
            Test the type of description
        '''
        description = getattr(self.new_place, "description")
        self.assertIsInstance(description, str)

    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_place, "name")
        self.assertIsInstance(name, str)

    def test_type_user_id(self):
        '''
            Test the type of user_id
        '''
        user_id = getattr(self.new_place, "user_id")
        self.assertIsInstance(user_id, str)

    def test_type_city_id(self):
        '''
            Test the type of city_id
        '''
        city_id = getattr(self.new_place, "city_id")
        self.assertIsInstance(city_id, str)
