#!/usr/bin/python3
"""Test cases for User model"""

import unittest
import os
import models
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class AmenityTest(unittest.TestCase):
    """Amenity test cases"""
    def test_Amenity_inherits_baseModel(self):
        """check that Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))

    def test_Amenity_instance_type(self):
        """check the instance's type"""
        amenity = Amenity()
        self.assertEqual(type(amenity), Amenity)

    def test_Amenity_id_attr(self):
        """check Amenity's id attribute is public"""
        amenity = Amenity()
        self.assertEqual(str, type(amenity.id))

    def test_Amenity_createAt_attr(self):
        """check Amenity's create_at attribute is public"""
        amenity = Amenity()
        self.assertEqual(datetime, type(amenity.created_at))

    def test_Amenity_updatedAt_attr(self):
        """check Amenity's updated_at attribute is public"""
        amenity = Amenity()
        self.assertEqual(datetime, type(amenity.updated_at))

    def test_Amenity_name_attr(self):
        """check Amenity's name attribute is public"""
        amenity = Amenity()
        self.assertEqual(str, type(amenity.name))

    def test_Amenity_two_amenitys_diffrent_ids(self):
        """check two amenitys have diffrent id"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_Amenity_init_unused_args(self):
        """check that args are not used"""
        obj1 = Amenity("val")
        self.assertNotIn("val", obj1.__dict__.values())

    def test_Amenity_two_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            Amenity().to_dict("val")

class AmenitySaveTest(unittest.TestCase):
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

    def test_Amenity_save_none_arg(self):
        """test save with None arg"""
        obj1 = Amenity()
        with self.assertRaises(TypeError):
            obj1.save(None)

    def test_Amenity_save_updatedAt_is_date(self):
        """check if save() saves datetime"""
        obj1 = Amenity()
        self.assertEqual(type(obj1.updated_at), datetime)

    def test_Amenity_save_updatedAt_changed(self):
        """check if save() changes the updated_at"""
        obj1 = Amenity()
        oldDate = obj1.updated_at
        obj1.save()
        newDate = obj1.updated_at
        self.assertTrue(oldDate < newDate)

    def test_Amenity_save_file_json(self):
        """test if instance is saved in the json file"""
        obj1 = Amenity()
        obj1.save()
        val = "Amenity." + obj1.id
        with open("file.json", "r") as file:
            self.assertIn(val, file.read())

    def test_Amenity_save_file_json_two_instances(self):
        """test if two instances is saved in the json file"""
        obj1 = Amenity()
        obj2 = Amenity()
        obj1.save()
        sleep(0.05)
        obj2.save()
        val1 = "Amenity." + obj1.id
        val2 = "Amenity." + obj2.id

        with open("file.json", "r") as file:
            self.assertIn(val1, file.read())
        with open("file.json", "r") as file:
            self.assertIn(val2, file.read())


class AmenityToDictTest(unittest.TestCase):
    """test to_dict()"""
    def test_Amenity_to_dict_vs_dunder_dict(self):
        "check obj.to_dict() is equal to obj.__dict__"
        obj1 = Amenity()
        self.assertNotEqual(obj1.to_dict(), obj1.__dict__)

    def test_Amenity_to_dict_with_arg(self):
        """test save with an arg"""
        obj1 = Amenity()
        with self.assertRaises(TypeError):
            obj1.save("val")

    def test_to_dict_attributes_type_str(self):
        """check if the attributes are strings"""
        obj = Amenity()
        obj_dict = obj.to_dict()
        self.assertEqual(str, type(obj_dict["id"]))
        self.assertEqual(str, type(obj_dict["created_at"]))
        self.assertEqual(str, type(obj_dict["updated_at"]))

    def test_Amenity_initialization_with_kwargs(self):
        """check Amenity when initializated with kwargs"""
        amenity = Amenity()
        date = datetime.now()
        amenity.id = "123-456-78"
        amenity.created_at = amenity.updated_at = date
        amenity.name = "fireplace"
        td = {
            "id": "123-456-78",
            "name": "fireplace",
            "created_at": date.isoformat(),
            "updated_at": date.isoformat(),
            "__class__": "Amenity"
        }
        self.assertDictEqual(amenity.to_dict(), td)
