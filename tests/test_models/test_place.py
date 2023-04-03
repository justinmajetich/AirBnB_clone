#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest


class test_Place(test_basemodel):
    """ """
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.obj = Place()
        cls.obj.name = "Apartment"
        cls.obj.city_id = "4534"
        cls.obj.user_id = "543"
        cls.obj.description = "Bright"
        cls.obj.number_rooms = 2
        cls.obj.number_bathrooms = 1
        cls.obj.max_guest = 4
        cls.obj.price_by_night = 150
        cls.obj.latitude = 54353.5435
        cls.obj.longitude = 5436.7657
        cls.obj.amenity_ids = []

    def is_subclass(self):
        """ tests subclass of BaseModel """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)

    def test_city_id(self):
        """ """
        self.assertEqual(type(self.obj.city_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.obj.user_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.obj.name), str)

    def test_description(self):
        """ """
        self.assertEqual(type(self.obj.description), str)

    def test_number_rooms(self):
        """ """
        self.assertEqual(type(self.obj.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        self.assertEqual(type(self.obj.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        self.assertEqual(type(self.obj.max_guest), int)

    def test_price_by_night(self):
        """ """
        self.assertEqual(type(self.obj.price_by_night), int)

    def test_latitude(self):
        """ """
        self.assertEqual(type(self.obj.latitude), float)

    def test_longitude(self):
        """ """
        self.assertEqual(type(self.obj.latitude), float)

    def test_amenity_ids(self):
        """ """
        self.assertEqual(type(self.obj.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
