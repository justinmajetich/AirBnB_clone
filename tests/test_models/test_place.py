#!/usr/bin/python3
""" Test module for place.py file. """

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Test class for place.py """

    def __init__(self, *args, **kwargs):
        """ test_Place class constructor"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Tests the city id """
        new = self.value()
        self.assertNotEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Tests the user id"""
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_name(self):
        """ Tests the name"""
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def test_description(self):
        """ Tests the description """
        new = self.value()
        self.assertNotEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Tests the number of rooms"""
        new = self.value()
        self.assertNotEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Tests number of bathrooms"""
        new = self.value()
        self.assertNotEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Tests the maximum number of guests"""
        new = self.value()
        self.assertNotEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Tests the price per night """
        new = self.value()
        self.assertNotEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Tests the latitude of the location """
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Tests longitude of house location """
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Tests the amenity id """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
