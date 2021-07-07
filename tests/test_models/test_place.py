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
        self.place.city_id = "1234-abcd"
        self.place.user_id = "4321-dcba"
        self.place.name = "Death Star"
        self.place.description = "UNLIMITED POWER!!!!!"
        self.place.number_rooms = 1000000
        self.place.number_bathrooms = 1
        self.place.max_guest = 607360
        self.place.price_by_night = 10
        self.place.latitude = 160.0
        self.place.longitude = 120.0
        self.place.amenity_ids = ["1324-lksdjkl"]

    def test_city_id(self):
        """ """
        new = self.place
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.place
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.place
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.place
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.place
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.place
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.place
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.place
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.place
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.place
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.place
        self.assertEqual(type(new.amenity_ids), list)
