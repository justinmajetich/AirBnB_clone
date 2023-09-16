#!/usr/bin/python3
"""Test cases for User model"""

import unittest
import os
import models
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class CityTest(unittest.TestCase):
    """City test cases"""
    def test_City_inherits_baseModel(self):
        """check that City inherits from BaseModel"""
        city = City()
        self.assertTrue(isinstance(city, BaseModel))

    def test_City_instance_type(self):
        """check the instance's type"""
        city = City()
        self.assertEqual(type(city), City)

    def test_City_id_attr(self):
        """check City's id attribute is public"""
        city = City()
        self.assertEqual(str, type(city.id))

    def test_City_createAt_attr(self):
        """check City's create_at attribute is public"""
        city = City()
        self.assertEqual(datetime, type(city.created_at))

    def test_City_updatedAt_attr(self):
        """check City's updated_at attribute is public"""
        city = City()
        self.assertEqual(datetime, type(city.updated_at))

    def test_City_name_attr(self):
        """check City's name attribute is public"""
        city = City()
        self.assertEqual(str, type(city.name))

    def test_City_state_id_attr(self):
        """check City's satte_id attribute is public"""
        city = City()
        self.assertEqual(str, type(city.state_id))

    def test_City_two_citys_diffrent_ids(self):
        """check two citys have diffrent id"""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_City_init_unused_args(self):
        """check that args are not used"""
        obj1 = City("val")
        self.assertNotIn("val", obj1.__dict__.values())

    def test_City_two_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            City().to_dict("val")

class CitySaveTest(unittest.TestCase):
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

    def test_City_save_none_arg(self):
        """test save with None arg"""
        obj1 = City()
        with self.assertRaises(TypeError):
            obj1.save(None)

    def test_City_save_updatedAt_is_date(self):
        """check if save() saves datetime"""
        obj1 = City()
        self.assertEqual(type(obj1.updated_at), datetime)

    def test_City_save_updatedAt_changed(self):
        """check if save() changes the updated_at"""
        obj1 = City()
        oldDate = obj1.updated_at
        obj1.save()
        newDate = obj1.updated_at
        self.assertTrue(oldDate < newDate)

    def test_City_save_file_json(self):
        """test if instance is saved in the json file"""
        obj1 = City()
        obj1.save()
        val = "City." + obj1.id
        with open("file.json", "r") as file:
            self.assertIn(val, file.read())

    def test_City_save_file_json_two_instances(self):
        """test if two instances is saved in the json file"""
        obj1 = City()
        obj2 = City()
        obj1.save()
        sleep(0.05)
        obj2.save()
        val1 = "City." + obj1.id
        val2 = "City." + obj2.id

        with open("file.json", "r") as file:
            self.assertIn(val1, file.read())
        with open("file.json", "r") as file:
            self.assertIn(val2, file.read())


class CityToDictTest(unittest.TestCase):
    """test to_dict()"""
    def test_City_to_dict_vs_dunder_dict(self):
        "check obj.to_dict() is equal to obj.__dict__"
        obj1 = City()
        self.assertNotEqual(obj1.to_dict(), obj1.__dict__)

    def test_City_to_dict_with_arg(self):
        """test save with an arg"""
        obj1 = City()
        with self.assertRaises(TypeError):
            obj1.save("val")

    def test_to_dict_attributes_type_str(self):
        """check if the attributes are strings"""
        obj = City()
        obj_dict = obj.to_dict()
        self.assertEqual(str, type(obj_dict["id"]))
        self.assertEqual(str, type(obj_dict["created_at"]))
        self.assertEqual(str, type(obj_dict["updated_at"]))

    def test_City_initialization_with_kwargs(self):
        """check City when initializated with kwargs"""
        city = City()
        date = datetime.now()
        city.id = "123-456-78"
        city.created_at = city.updated_at = date
        city.state_id = "NA"
        city.name = "Nagasaki"
        td = {
            "id": "123-456-78",
            "state_id": "NA",
            "name": "Nagasaki",
            "created_at": date.isoformat(),
            "updated_at": date.isoformat(),
            "__class__": "City"
        }
        self.assertDictEqual(city.to_dict(), td)
