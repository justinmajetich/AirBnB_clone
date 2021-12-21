#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from unittest.mock import patch
import pycodestyle
import models


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
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    @classmethod
    def setup_class(self):
        """Setup for docstring"""
        self.user_1 = Place()

    def test_docstrings(self):
        """test documentation"""
        self.assertIsNotNone(Place.__doc__, "city.py needs a docstring")

    def test_instance(self):
        """check if user is an instance of BaseModel"""
        user = Place()
        self.assertIsInstance(user, Place)
        self.assertTrue(issubclass(type(user), BaseModel))
        self.assertEqual(str(type(user)), "<class 'models.place.Place'>")

    """Testing City class"""
    def test_instances(self):
        with patch('models.place'):
            instance = Place()
            self.assertEqual(type(instance), Place)
            instance.name = "OnePiece"
            instance.description = "Amazing place"
            instance.number_rooms = 20
            instance.number_bathrooms = 15
            instance.max_guest = 9
            instance.price_by_night = 100
            instance.latitude = 250.3
            instance.longitude = 340.2
            instance.amenity_ids = ["3344", "2021", "3012"]
            expectec_attrs_types = {
                    "id": str,
                    "created_at": datetime,
                    "updated_at": datetime,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list
                    }
            inst_dict = instance.to_dict()
            expected_dict_attrs = [
                    "id",
                    "created_at",
                    "updated_at",
                    "name",
                    "description",
                    "number_rooms",
                    "number_bathrooms",
                    "max_guest",
                    "price_by_night",
                    "latitude",
                    "longitude",
                    "amenity_ids",
                    "__class__"
                    ]
            self.assertCountEqual(inst_dict.keys(), expected_dict_attrs)
            self.assertEqual(inst_dict['name'], 'OnePiece')
            self.assertEqual(inst_dict['description'], 'Amazing place')
            self.assertEqual(inst_dict['number_rooms'], 20)
            self.assertEqual(inst_dict['number_bathrooms'], 15)
            self.assertEqual(inst_dict['max_guest'], 9)
            self.assertEqual(inst_dict['price_by_night'], 100)
            self.assertEqual(inst_dict['latitude'], 250.3)
            self.assertEqual(inst_dict['longitude'], 340.2)
            self.assertEqual(inst_dict['amenity_ids'],
                             ["3344", "2021", "3012"])
            self.assertEqual(inst_dict['__class__'], 'Place')

            for attr, types in expectec_attrs_types.items():
                with self.subTest(attr=attr, typ=types):
                    self.assertIn(attr, instance.__dict__)
                    self.assertIs(type(instance.__dict__[attr]), types)
            self.assertEqual(instance.name, "OnePiece")
            self.assertEqual(instance.description, "Amazing place")
            self.assertEqual(instance.number_rooms, 20)
            self.assertEqual(instance.number_bathrooms, 15)
            self.assertEqual(instance.max_guest, 9)
            self.assertEqual(instance.price_by_night, 100)
            self.assertEqual(instance.latitude, 250.3)
            self.assertEqual(instance.longitude, 340.2)
            self.assertEqual(instance.amenity_ids, ["3344", "2021", "3012"])

    def test_Place_id_and_createat(self):
        """testing id for every user"""
        user_1 = Place()
        sleep(2)
        user_2 = Place()
        sleep(2)
        user_3 = Place()
        sleep(2)
        list_users = [user_1, user_2, user_3]
        for instance in list_users:
            user_id = instance.id
            with self.subTest(user_id=user_id):
                self.assertIs(type(user_id), str)
        self.assertNotEqual(user_1.id, user_2.id)
        self.assertNotEqual(user_1.id, user_3.id)
        self.assertNotEqual(user_2.id, user_3.id)
        self.assertTrue(user_1.created_at <= user_2.created_at)
        self.assertTrue(user_2.created_at <= user_3.created_at)
        self.assertNotEqual(user_1.created_at, user_2.created_at)
        self.assertNotEqual(user_1.created_at, user_3.created_at)
        self.assertNotEqual(user_3.created_at, user_2.created_at)

    def test_str_method(self):
        """
        Testin str magic method
        """
        inst = Place()
        str_output = "[Place] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(str_output, str(inst))

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Testing save method and if it update"""
        instance5 = Place()
        created_at = instance5.created_at
        sleep(2)
        updated_at = instance5.updated_at
        instance5.save()
        new_created_at = instance5.created_at
        sleep(2)
        new_updated_at = instance5.updated_at
        self.assertNotEqual(updated_at, new_updated_at)
        self.assertEqual(created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)


if __name__ == '__main__':
    unittest.main()
