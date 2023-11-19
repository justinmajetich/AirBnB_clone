#!/usr/bin/python3
"""
Test module for the Place calss using the unittest module
"""
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class test_Place(TestBaseModel):
    """A Subclass of uinttest class that test the Place class"""

    def __init__(self, *args, **kwargs):
        """init the Place class and its Super"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test the Place city_id attribute"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Ttest the user_id attribute"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Test the Place name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Test the Placs description attribute"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Test the number_rooms attribute """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test the number_bathrooms attribute"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Test the max_quest attribute"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Test the price_by_night attribute"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Test the latitude attribute"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Test the longitude attribute"""
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ Test the amenity_ids attribute"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
