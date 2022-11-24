#!/usr/bin/python3
"""test for place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """test class for place class """

    def __init__(self, *args, **kwargs):
        """test """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test """
        new = self.value(city_id="askjhhd")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test """
        new = self.value(user_id="akjhklds")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ test"""
        new = self.value(name="name")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test """
        new = self.value(description="good")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test"""
        new = self.value(number_rooms=2)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test """
        new = self.value(number_bathrooms=1)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test """
        new = self.value(max_guest=6)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test """
        new = self.value(price_by_night=100)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test """
        new = self.value(latitude=10.2)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ test """
        new = self.value(longitude=11.121)
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """test """
        new = self.value(amenity_ids=["tv", "wifi"])
        self.assertEqual(type(new.amenity_ids), list)