#!/usr/bin/python3
""" Unittest for class Place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Unittest for class Place"""

    def __init__(self, *args, **kwargs):
        """ test initialisation of class """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test type of city_id attribute"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ test type of user_id attribute"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ test type of name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test type of description attribute"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test type of number rooms attribute"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ test type of number bathrooms attribute"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ test of type of max_guest attribute"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ test of price by night type attribute"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ test of latitude attribute"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ test type of longitude attribute"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ test of type amenity_ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
