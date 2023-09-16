#!/usr/bin/python3
"""Test cases for User model"""

import unittest
import os
import models
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class UserTest(unittest.TestCase):
    """User test cases"""
    def test_User_inherits_baseModel(self):
        """check that User inherits from BaseModel"""
        user = User()
        self.assertTrue(isinstance(user, BaseModel))

    def test_User_instance_type(self):
        """check the instance's type"""
        user = User()
        self.assertEqual(type(user), User)

    def test_User_id_attr(self):
        """check User's id attribute is public"""
        user = User()
        self.assertEqual(str, type(user.id))

    def test_User_createAt_attr(self):
        """check User's create_at attribute is public"""
        user = User()
        self.assertEqual(datetime, type(user.created_at))

    def test_User_updatedAt_attr(self):
        """check User's updated_at attribute is public"""
        user = User()
        self.assertEqual(datetime, type(user.updated_at))

    def test_User_password_attr(self):
        """check User's password attribute is public"""
        user = User()
        self.assertEqual(str, type(user.password))

    def test_User_email_attr(self):
        """check User's email attribute is public"""
        user = User()
        self.assertEqual(str, type(user.email))

    def test_User_first_name_attr(self):
        """check User's first_name attribute is public"""
        user = User()
        self.assertEqual(str, type(user.first_name))

    def test_User_last_name_attr(self):
        """check User's last_name attribute is public"""
        user = User()
        self.assertEqual(str, type(user.last_name))

    def test_User_two_users_diffrent_ids(self):
        """check two users have diffrent id"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_User_init_unused_args(self):
        """check that args are not used"""
        obj1 = User("val")
        self.assertNotIn("val", obj1.__dict__.values())

    def test_User_two_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            User().to_dict("val")

class UserSaveTest(unittest.TestCase):
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

    def test_User_save_none_arg(self):
        """test save with None arg"""
        obj1 = User()
        with self.assertRaises(TypeError):
            obj1.save(None)

    def test_User_save_updatedAt_is_date(self):
        """check if save() saves datetime"""
        obj1 = User()
        self.assertEqual(type(obj1.updated_at), datetime)

    def test_User_save_updatedAt_changed(self):
        """check if save() changes the updated_at"""
        obj1 = User()
        oldDate = obj1.updated_at
        obj1.save()
        newDate = obj1.updated_at
        self.assertTrue(oldDate < newDate)

    def test_User_save_file_json(self):
        """test if instance is saved in the json file"""
        obj1 = User()
        obj1.save()
        val = "User." + obj1.id
        with open("file.json", "r") as file:
            self.assertIn(val, file.read())

    def test_User_save_file_json_two_instances(self):
        """test if two instances is saved in the json file"""
        obj1 = User()
        obj2 = User()
        obj1.save()
        sleep(0.05)
        obj2.save()
        val1 = "User." + obj1.id
        val2 = "User." + obj2.id

        with open("file.json", "r") as file:
            self.assertIn(val1, file.read())
        with open("file.json", "r") as file:
            self.assertIn(val2, file.read())


class UserToDictTest(unittest.TestCase):
    """test to_dict()"""
    def test_User_to_dict_vs_dunder_dict(self):
        "check obj.to_dict() is equal to obj.__dict__"
        obj1 = User()
        self.assertNotEqual(obj1.to_dict(), obj1.__dict__)

    def test_User_to_dict_with_arg(self):
        """test save with an arg"""
        obj1 = User()
        with self.assertRaises(TypeError):
            obj1.save("val")

    def test_to_dict_attributes_type_str(self):
        """check if the attributes are strings"""
        obj = User()
        obj_dict = obj.to_dict()
        self.assertEqual(str, type(obj_dict["id"]))
        self.assertEqual(str, type(obj_dict["created_at"]))
        self.assertEqual(str, type(obj_dict["updated_at"]))

    def test_User_initialization_with_kwargs(self):
        """check User when initializated with kwargs"""
        user = User()
        date = datetime.now()
        user.id = "123-456-78"
        user.created_at = user.updated_at = date
        user.first_name = "John"
        user.last_name = "Doe"
        user.password = "pass"
        user.email = "some@mail.com"
        td = {
            "id": "123-456-78",
            "first_name": "John",
            "last_name": "Doe",
            "password": "pass",
            "email": "some@mail.com",
            "created_at": date.isoformat(),
            "updated_at": date.isoformat(),
            "__class__": "User"
        }
        self.assertDictEqual(user.to_dict(), td)
