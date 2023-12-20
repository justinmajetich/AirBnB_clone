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

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertIsNone(new.city_id)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertIsNone(new.user_id)

    def test_name(self):
        """ """
        new = self.value()
        self.assertIsNone(new.name)

    def test_description(self):
        """ """
        new = self.value()
        self.assertIsNone(new.description)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.__class__.number_rooms.default.arg), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(
            type(new.__class__.number_bathrooms.default.arg), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.__class__.max_guest.default.arg), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.__class__.price_by_night.default.arg), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertIsNone(new.latitude)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertIsNone(new.latitude)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
