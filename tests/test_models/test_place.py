#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from tests.test_models.test_city import new as new_C
from tests.test_models.test_user import new as new_U
import os
import unittest

new = Place(city_id=new_C.id, user_id=new_U.id, name='KFC',
            description='Fried', number_rooms=2,
            number_bathrooms=1, max_guest=30,
            price_by_night=5, latitude=1.2, logitude=3.4)


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE"), "Using FileStorage")
    def test_amenity_ids(self):
        """ """
        self.assertEqual(type(new.amenity_ids), list)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") is None, "Using \
                     DBStorage")
    def test_amenities(self):
        """ """
        self.assertEqual(type(new.amenities), list)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") is None, "Using \
                     DBStorage")
    def test_reviews(self):
        """ """
        self.assertEqual(type(new.reviews), list)
