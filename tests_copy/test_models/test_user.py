#!/usr/bin/python3
"""
Unittest for the Class "User"
"""

import unittest
import time
import datetime
from models.user import User
import models


class Test_user_attr(unittest.TestCase):
    """This class defines unittests for the different attributes both inherited
    and unique for the User Class"""

    def test_uniq_time(self):
        """This function tests for the uniquenss of time creation"""
        user1 = User()
        time.sleep(0.001)
        user2 = User()
        self.assertNotEqual(user1.created_at, user2.created_at)

    def test_uniq_id(self):
        """This function tests for the uniqueness of the id"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_custom_id(self):
        """This function creates a User with a specific ID"""
        usr = User()
        usr.id = "123456"
        self.assertEqual(usr.id, "123456")

    def test_type_id(self):
        """This function tests the type of id attr"""
        self.assertIs(type(User().id), str)

    def test_type_created_at(self):
        """This function tests the type of created_at attr"""
        self.assertIs(type(User().created_at), datetime.datetime)

    def test_type_updated_at(self):
        """This function tests for the type of updated_at attr"""
        self.assertIs(type(User().updated_at), datetime.datetime)

    def test_type_email(self):
        """This function tests the type of email attr"""
        self.assertIs(type(User().email), str)

    def test_type_password(self):
        """This function tests for the type of password attr"""
        self.assertIs(type(User().password), str)

    def test_type_first_name(self):
        """This function tests the type first_name attr"""
        self.assertIs(type(User().first_name), str)

    def test_type_last_name(self):
        """This function tests the type last_name attr"""
        self.assertIs(type(User().last_name), str)

    def test_obj_storage(self):
        """This function tests that an object is automatically saved in
        the ___objects attr of storage instance"""
        usr = User()
        self.assertIn(usr, models.storage.all().values())

    def test_type_class(self):
        """This function tests the type of an instance created"""
        self.assertIs(type(User()), User)

    def test_str(self):
        """This funtion tests string representation of a BaseModel"""
        usr = User()
        usr.id = "123456"
        tdy = datetime.datetime.today()
        usr.created_at = usr.updated_at = tdy
        self.assertIn("[User] (123456)", usr.__str__())
        self.assertIn("'id': '123456'", usr.__str__())
        self.assertIn("'created_at': " + repr(tdy), usr.__str__())
        self.assertIn("'updated_at': " + repr(tdy), usr.__str__())


class Test_instantation(unittest.TestCase):
    """Thid class tests the instantation of a User class"""

    def test_init_kwargs(self):
        """This function create a User with kwargs"""
        tdy = datetime.datetime.today()
        usr = User(id="123456", created_at=tdy.isoformat(),
                   updated_at=tdy.isoformat())
        self.assertEqual(usr.id, "123456")
        self.assertEqual(usr.created_at, tdy)
        self.assertEqual(usr.updated_at, tdy)

    def test_init_args(self):
        """This function creates a User without args"""
        tdy = datetime.datetime.today()
        usr = User("7890", id="4567",
                   created_at=tdy.isoformat(), updated_at=tdy.isoformat())
        self.assertEqual(usr.id, "4567")
        self.assertEqual(usr.created_at, tdy)
        self.assertEqual(usr.updated_at, tdy)

    def teat_init_class(self):
        """This function tests giving args a class key"""
        usr1 = User()
        dict_usr1 = usr1.to_dict()
        dict_usr1['__class__'] = "BaseModel"
        usr2 = User(**dict_usr1)
        dict_usr2 = usr2.to_dict()
        self.assertEqual(dict_usr2['__class__'], "User")


class Test_save(unittest.TestCase):
    """This class tests the instance method save(self)"""

    def test_save(self):
        """This function tests updating the time"""
        usr = User()
        old_time = usr.updated_at
        usr.save()
        self.assertNotEqual(usr.updated_at, old_time)

    def test_two_save(self):
        """This function tests updates the time twice"""
        usr = User()
        first_time = usr.updated_at
        usr.save()
        self.assertNotEqual(usr.updated_at, first_time)
        second_time = usr.updated_at
        usr.save()
        self.assertNotEqual(usr.updated_at, second_time)

    def test_save_args(self):
        """This function give save method an argument"""
        with self.assertRaises(TypeError):
            User().save("arg")

    def test_save_file(self):
        """This function tests saving into a JSOM file"""
        usr = User()
        usr.save()
        with open(models.storage._FileStorage__file_path,
                  encoding="utf-8") as f:
            self.assertIn("User." + usr.id, f.read())


class Test_to_dict(unittest.TestCase):
    """unittests for the instance method to_dict"""

    def test_type_dict(self):
        """This function tests the type of to_dict return value"""
        self.assertIs(type(User().to_dict()), dict)

    def test_contents_dict(self):
        """This function tests the contents of a dictionary"""
        usr = User()
        self.assertIn('updated_at', usr.to_dict())
        self.assertIn('__class__', usr.to_dict())
        self.assertIn('id', usr.to_dict())
        self.assertIn('created_at', usr.to_dict())

    def test_dynamic_dict(self):
        """This function tests the dynamic creation of attributes in dict"""
        usr = User()
        usr.nickname = "mr.awesome"
        usr.num = 456
        self.assertIn('nickname', usr.to_dict())
        self.assertIn('num', usr.to_dict())

    def test_type_time_in_dict(self):
        """This function tests the type of created_at and updated_at
        in dict"""
        usr = User()
        usr_dict = usr.to_dict()
        self.assertIs(type(usr_dict['id']), str)
        self.assertIs(type(usr_dict['created_at']), str)
        self.assertIs(type(usr_dict['updated_at']), str)

    def test_dict_kwargs(self):
        """This function create a User with kwargs and tests its dict"""
        tdy = datetime.datetime.today()
        usr = User(id="123456", created_at=tdy.isoformat(),
                   updated_at=tdy.isoformat(), email="airbnb2@mail.com",
                   first_name="John", last_name="Doe", password="root")
        usr_dict = usr.to_dict()
        self.assertIn('email', usr_dict)
        self.assertIn('first_name', usr_dict)
        self.assertIn('last_name', usr_dict)
        self.assertIn('password', usr_dict)

    def test_full_dict(self):
        """This function tests creation of a dictionary"""
        usr = User()
        usr.id = "123456"
        tdy = datetime.datetime.today()
        usr.created_at = usr.updated_at = tdy
        dict_usr = {'__class__': 'User',
                    'updated_at': tdy.isoformat(),
                    'created_at': tdy.isoformat(),
                    'id': "123456"}
        self.assertDictEqual(usr.to_dict(), dict_usr)

    def test_dict_class(self):
        """This function tests that __dict__ repr and to_dict()
        are different"""
        usr = User()
        self.assertNotEqual(usr.__dict__, usr.to_dict())

    def test_to_dict_arg(self):
        """This function tests giving the instance method to_dict
        arguments"""
        with self.assertRaises(TypeError):
            User().to_dict("arg")


if __name__ == '__main__':
    unittest.main()
