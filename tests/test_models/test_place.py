#!/usr/bin/python3
""" Tests for place class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest

class test_Place(unittest.TestCase,test_basemodel):
    """ class for test_place"""

    def __init__(self, *args, **kwargs):
        """initialize class test_place """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test city_id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ test city_id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test number of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ test number_bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test max_guest """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test city_id """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test latitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test longitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test amenity_id """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
