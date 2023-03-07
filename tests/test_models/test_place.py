#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class test_Place(TestBaseModel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        if new.city_id is None:
            new.city_id = ''
        self.assertIsInstance(new.city_id, str)
        self.assertEqual(new.city_id, '')

    def test_user_id(self):
        """ """
        new = self.value()
        if new.user_id is None:
            new.user_id = ''
        self.assertIsInstance(new.user_id, str)
        self.assertEqual(new.user_id, '')

    def test_name(self):
        """ """
        new = self.value()
        if new.name is None:
            new.name = ''
        self.assertIsInstance(new.name, str)
        self.assertEqual(new.name, '')

    def test_description(self):
        """ """
        new = self.value()
        if new.description is None:
            new.description = ''
        self.assertIsInstance(new.description, str)
        self.assertEqual(new.description, '')

    def test_number_rooms(self):
        """ """
        new = self.value()
        if new.number_rooms is None:
            new.number_rooms = 0
        self.assertIsInstance(new.number_rooms, int)
        self.assertEqual(new.number_rooms, 0)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        if new.number_bathrooms is None:
            new.number_bathrooms = 0
        self.assertIsInstance(new.number_bathrooms, int)
        self.assertEqual(new.number_bathrooms, 0)

    def test_max_guest(self):
        """ """
        new = self.value()
        if new.max_guest is None:
            new.max_guest = 0
        self.assertIsInstance(new.max_guest, int)
        self.assertEqual(new.max_guest, 0)

    def test_price_by_night(self):
        """Test that price_by_night is an integer & has default value of 0"""
        new = self.value()
        if new.price_by_night is None:
            new.price_by_night = 0
        self.assertIsInstance(new.price_by_night, int)
        self.assertEqual(new.price_by_night, 0)

    def test_latitude(self):
        """ """
        new = self.value()
        if new.latitude is None:
            new.latitude = 0.0
        self.assertIsInstance(new.latitude, float)
        self.assertEqual(new.latitude, 0.0)

    def test_longitude(self):
        """ """
        new = self.value()
        if new.longitude is None:
            new.longitude = 0.0
        self.assertIsInstance(new.longitude, float)
        self.assertEqual(new.longitude, 0.0)

    def test_amenities(self):
        """Test that amenities is a list"""
        new = self.value()
        self.assertEqual(type(new.amenities), list)