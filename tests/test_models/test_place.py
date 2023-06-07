#!/usr/bin/python3
"""
This module defines test for the Place model
"""

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """
    This class defines specific tests for the Place model
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the class
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Ensure that the `city_id` attribute of this class is a string
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Ensure that the `user_id` attribute of this class is a string
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        Ensure that the `name` attribute of this class is a string
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        Ensure that the `description` attribute of this class is a string
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        Ensure that the `number_rooms` attribute of this class is an integer
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Ensure that the `number_bathrooms` attribute of this class \
is an integer
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        Ensure that the `max_guest` attribute of this class is an integer
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        Ensure that the `price_by_night` attribute of this class is an integer
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        Ensure that the `lattitude` attribute of this class is a float
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Ensure that the `longitude` attribute of this class is a float
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """
        Ensure that the `amenity_ids` attribute of this class is a list
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
