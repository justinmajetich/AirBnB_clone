#!/usr/bin/python3
"""This tests for Place """
import unittest
import os
import pep8
from os import getenv
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """This tests for class Place is subclass of BaseModel"""

    def __init__(self, *args, **kwargs):
        """This initializes the test process  """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """This tests for the functionality of city_id of Place class"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """This tests if the method usr_id works """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Tests The behavior of attribute type name of class Place"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """This tests the behavior of the Place class desc attribute"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """This tests for attribute type number_room """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Test the attribute type number_bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """This checks for max_guest attribute works """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """This tests price_by_night attribute of Place class works"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Checks if latitude of Place class is properly set"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Checks if longitude of Place class is properly set"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Checks if amenity_ids of Place class is properly set"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_Place(self):
        """This tests if the save works"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_attributes_Place(self):
        """Tests for amenity attributes of class Place are working"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_to_dict_Place(self):
        """Tests if dictionary is properly set"""
        self.assertEqual('to_dict' in dir(self.place), True)

    def test_is_subclass_Place(self):
        """test if Place is subclass of Basemodel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)


if __name__ == "__main__":
    unittest.main()
