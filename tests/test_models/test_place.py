#!/usr/bin/python3
"""
    Test Case For Place Model and its Test
"""
from models.base_model import BaseModel
from models.place import Place
import unittest
import inspect
import time
from datetime import datetime
import pep8 as pcs
from unittest import mock
import models


class TestPlace(unittest.TestCase):
    """
        unitesst for Place class
    """

    def issub_class(self):
        """
            test if Place class is sub class of base model
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "update_at"))

    def test_city_id_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        if models.storage_type == "db":
            self.assertEqual(place.city_id, None)

    def test_user_id_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        if models.storage_type == "db":
            self.assertEqual(place.user_id, None)
        else:
            pass

    def test_name_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        if models.storage_type == "db":
            self.assertEqual(place.name, None)
        else:
            pass

    def test_description_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        if models.storage_type == "db":
            self.assertEqual(place.description, None)
        else:
            pass

    def test_number_rooms_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        if models.storage_type == "db":
            self.assertEqual(place.number_rooms, None)

    def test_number_bathrooms_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        if models.storage_type == "db":
            self.assertEqual(place.number_bathrooms, None)
        else:
            pass

    def test_max_guest_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        if models.storage_type == "db":
            self.assertEqual(place.max_guest, None)
        else:
            pass

    def test_price_by_night_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        if models.storage_type == "db":
            self.assertEqual(place.price_by_night, None)
        else:
            pass

    def test_latitude_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        if models.storage_type == "db":
            self.assertEqual(place.latitude, None)
        else:
            pass

    def test_latitude_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        if models.storage_type == "db":
            self.assertEqual(place.longitude, None)
        else:
            pass

    def test_amenity_ids_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        if models.storage_type == "db":
            self.assertEqual(len(place.amenity_ids), 0)
        else:
            pass

    def test_to_dictPlace(self):
        """
            test to dict method with Place and the type
            and content
        """
        place = Place()
        dict_cont = place.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in place.__dict__:
            self.assertTrue(attr in dict_cont)
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """
            test the returned dictionar values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        place = Place()
        dict_con = place.to_dict()
        self.assertEqual(dict_con["__class__"], "Place")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
            dict_con["created_at"],
            place.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_con["updated_at"],
            place.updated_at.strftime(time_format))
