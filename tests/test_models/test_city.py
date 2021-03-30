#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel
import unittest
import os

type_storage = os.getenv('HBNB_TYPE_STORAGE')


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class test_city_v2(unittest.TestCase):
    """ Class test City"""

    def test001(self):
        """Check if City is child of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test002(self):
        """ Check City default attributes """
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(city.name is "")
        self.assertTrue(city.state_id is "")

    def test003(self):
        """ Check State when type storage is db"""
        city = City()
        if (type_storage == 'db'):
            self.assertTrue(city.name is None)
            self.assertTrue(city.state_id is None)

    def test004(self):
        """ Check to_dict() function """
        city = City()
        city_dict = city.to_dict()
        self.assertTrue(type(city_dict) is dict)
        self.assertFalse("_sa_instance_state" in city_dict)

    def test005(self):
        """ Check save() """
        city = City()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)
