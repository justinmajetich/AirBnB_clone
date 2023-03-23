#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test case"""

    def __init__(self, *args, **kwargs):
        """attribute initialization"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """check if the type is a string"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """check if the type is a string"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """check if the type is a string"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """check if the type is a string"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """check if the type is a integer"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """check if the type is a integer"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """check if the type is a integer"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """check if the type is a integer"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """check if the type is a float"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """check if the type is a float"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """check if the type is a list"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
