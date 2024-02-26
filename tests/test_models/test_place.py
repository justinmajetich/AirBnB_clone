#!/usr/bin/python3
""" Module for place unittesting"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest
import models.place
import pep8


class test_Place(test_basemodel):
    """ unittests for place"""

    def __init__(self, *args, **kwargs):
        """ instantiates place for testing"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ tests proper funcionality of city id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ tests proper creation of user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ test proper creation of place name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test proper creation of place description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test proper creation of number of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ test proper creation of number of bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ test proper creation of number of guests"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ tests proper creation of price by night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ tests proper creation of latitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ tests proper creation of longitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ tests proper creation amenity id """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in place class"""

    def test_module_doc(self):
        """ checks for module doc"""
        self.assertGreaterEqual(len(models.place.__doc__), 1)

    def test_class_doc(self):
        """ checks for class doc"""
        self.assertGreaterEqual(len(Place.__doc__), 1)


class TestPlaceepep8(unittest.TestCase):
    """ tests place class for pep8 compliance"""

    def test_pep8_compliance(self):
        """ test to ensure models/places.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_place.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")