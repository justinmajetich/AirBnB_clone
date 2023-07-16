#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        self.place = self.value()
        self.place.city_id = "0001"
        self.place.user_id = "0002"
        self.place.name = "My Place"
        self.place.description = "Awesome Place"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 37.7749
        self.place.longitude = 122.4194
        self.place.amenity_ids = ["0003", "0004"]

    def test_city_id(self):
        """ """
        self.assertEqual(type(self.place.city_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.place.user_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.place.name), str)

    def test_description(self):
        """ """
        self.assertEqual(type(self.place.description), str)

    def test_number_rooms(self):
        """ """
        self.assertEqual(type(self.place.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        self.assertEqual(type(self.place.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        self.assertEqual(type(self.place.max_guest), int)

    def test_price_by_night(self):
        """ """
        self.assertEqual(type(self.place.price_by_night), int)

    def test_latitude(self):
        """ """
        self.assertEqual(type(self.place.latitude), float)

    def test_longitude(self):
        """ """
        self.assertEqual(type(self.place.longitude), float)

    def test_amenity_ids(self):
        """ """
        self.assertEqual(type(self.place.amenity_ids), list)
