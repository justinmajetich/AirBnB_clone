#!/usr/bin/python3
""" Unittests for Place class"""
import unittest
from models.place import Place
from tests.test_models.test_base_model import test_basemodel


class test_Place(test_basemodel):
    """ Test for place class"""

    def __init__(self, *args, **kwargs):
        """ Test Place instantiation"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test city id type """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Test user id type """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Test name type """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Test description type"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Test number rooms type """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test number_bathrooms type """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Test max guests type """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Test price by night type """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Test latitude type """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Test longitude type """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Test amenity ids type """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
