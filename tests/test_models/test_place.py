#!/usr/bin/python3
"""Test cases for User model"""

import unittest
import os
import models
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class PlaceTest(unittest.TestCase):
    """Place test cases"""
    def test_Place_inherits_baseModel(self):
        """check that Place inherits from BaseModel"""
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))

    def test_Place_instance_type(self):
        """check the instance's type"""
        place = Place()
        self.assertEqual(type(place), Place)

    def test_Place_id_attr(self):
        """check Place's id attribute is public"""
        place = Place()
        self.assertEqual(str, type(place.id))

    def test_Place_createAt_attr(self):
        """check Place's create_at attribute is public"""
        place = Place()
        self.assertEqual(datetime, type(place.created_at))

    def test_Place_updatedAt_attr(self):
        """check Place's updated_at attribute is public"""
        place = Place()
        self.assertEqual(datetime, type(place.updated_at))

    def test_Place_city_id_attr(self):
        """check Place's name attribute is public"""
        place = Place()
        self.assertEqual(str, type(place.city_id))

    def test_Place_user_id_attr(self):
        """check Place's user_id attribute is public"""
        place = Place()
        self.assertEqual(str, type(place.user_id))

    def test_Place_name_attr(self):
        """check Place's name attribute is public"""
        place = Place()
        self.assertEqual(str, type(place.name))

    def test_Place_description_attr(self):
        """check Place's description attribute is public"""
        place = Place()
        self.assertEqual(str, type(place.description))

    def test_Place_number_rooms_attr(self):
        """check Place's number_rooms attribute is public"""
        place = Place()
        self.assertEqual(int, type(place.number_rooms))

    def test_Place_number_bathrooms_attr(self):
        """check Place's number_bathrooms attribute is public"""
        place = Place()
        self.assertEqual(int, type(place.number_bathrooms))

    def test_Place_max_guest_attr(self):
        """check Place's max_guest attribute is public"""
        place = Place()
        self.assertEqual(int, type(place.max_guest))

    def test_Place_price_bynight_attr(self):
        """check Place's price_by_night attribute is public"""
        place = Place()
        self.assertEqual(int, type(place.price_by_night))

    def test_Place_latitude_attr(self):
        """check Place's latitude attribute is public"""
        place = Place()
        self.assertEqual(float, type(place.latitude))

    def test_Place_longitude_attr(self):
        """check Place's longitude attribute is public"""
        place = Place()
        self.assertEqual(float, type(place.longitude))

    def test_Place_amenity_ids_attr(self):
        """check Place's amenity_ids attribute is public"""
        place = Place()
        self.assertEqual(list, type(place.amenity_ids))

    def test_Place_two_places_diffrent_ids(self):
        """check two places have diffrent id"""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_Place_init_unused_args(self):
        """check that args are not used"""
        obj1 = Place("val")
        self.assertNotIn("val", obj1.__dict__.values())

    def test_Place_two_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            Place().to_dict("val")


class PlaceSaveTest(unittest.TestCase):
    """test cases for Uer.save() method"""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "_file.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("_file.json", "file.json")
        except IOError:
            pass

    def test_Place_save_none_arg(self):
        """test save with None arg"""
        obj1 = Place()
        with self.assertRaises(TypeError):
            obj1.save(None)

    def test_Place_save_updatedAt_is_date(self):
        """check if save() saves datetime"""
        obj1 = Place()
        self.assertEqual(type(obj1.updated_at), datetime)

    def test_Place_save_updatedAt_changed(self):
        """check if save() changes the updated_at"""
        obj1 = Place()
        oldDate = obj1.updated_at
        obj1.save()
        newDate = obj1.updated_at
        self.assertTrue(oldDate < newDate)

    def test_Place_save_file_json(self):
        """test if instance is saved in the json file"""
        obj1 = Place()
        obj1.save()
        val = "Place." + obj1.id
        with open("file.json", "r") as file:
            self.assertIn(val, file.read())

    def test_Place_save_file_json_two_instances(self):
        """test if two instances is saved in the json file"""
        obj1 = Place()
        obj2 = Place()
        obj1.save()
        sleep(0.05)
        obj2.save()
        val1 = "Place." + obj1.id
        val2 = "Place." + obj2.id

        with open("file.json", "r") as file:
            self.assertIn(val1, file.read())
        with open("file.json", "r") as file:
            self.assertIn(val2, file.read())


class PlaceToDictTest(unittest.TestCase):
    """test to_dict()"""
    def test_Place_to_dict_vs_dunder_dict(self):
        "check obj.to_dict() is equal to obj.__dict__"
        obj1 = Place()
        self.assertNotEqual(obj1.to_dict(), obj1.__dict__)

    def test_Place_to_dict_with_arg(self):
        """test save with an arg"""
        obj1 = Place()
        with self.assertRaises(TypeError):
            obj1.save("val")

    def test_to_dict_attributes_type_str(self):
        """check if the attributes are strings"""
        obj = Place()
        obj_dict = obj.to_dict()
        self.assertEqual(str, type(obj_dict["id"]))
        self.assertEqual(str, type(obj_dict["created_at"]))
        self.assertEqual(str, type(obj_dict["updated_at"]))

    def test_Place_initialization_with_kwargs(self):
        """check Place when initializated with kwargs"""
        place = Place()
        date = datetime.now()
        place.id = "123-456-78"
        place.created_at = place.updated_at = date
        place.city_id = "NA"
        place.user_id = "user.123"
        place.name = "place"
        place.description = "description"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 2
        place.price_by_night = 25
        place.latitude = 48.5
        place.longitude = 15.9
        place.amenity_ids = ["Amenity.bc261e64-8dce-428c-a068-7f498743149f"]
        td = {
            "id": "123-456-78",
            "created_at": date.isoformat(),
            "updated_at": date.isoformat(),
            "__class__": "Place",
            "city_id": "NA",
            "user_id": "user.123",
            "name": "place",
            "description": "description",
            "number_rooms": 2,
            "number_bathrooms": 1,
            "max_guest": 2,
            "price_by_night": 25,
            "latitude": 48.5,
            "longitude": 15.9,
            "amenity_ids": ["Amenity.bc261e64-8dce-428c-a068-7f4987431\
49f"]
        }
        self.assertDictEqual(place.to_dict(), td)
