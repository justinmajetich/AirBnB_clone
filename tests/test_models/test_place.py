#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Tests for the class Place"""

    def __init__(self, *args, **kwargs):
        """ Initialization of the test Place"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test to check for the City id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Test to check for the User id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Test to check for the name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Test to check for the description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Test to check for the number of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test to check for the number of bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Test to check for the max number of guests"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Test to check for the price by night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Test to check for the latitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Test to check for the longitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Test to check for the Amenity ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
