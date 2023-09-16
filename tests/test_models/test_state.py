#!/usr/bin/python3
"""Test cases for State model"""

import unittest
import os
import models
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class StateTest(unittest.TestCase):
    """State test cases"""
    def test_State_inherits_baseModel(self):
        """check that State inherits from BaseModel"""
        state = State()
        self.assertTrue(isinstance(state, BaseModel))

    def test_State_instance_type(self):
        """check the instance's type"""
        state = State()
        self.assertEqual(type(state), State)

    def test_State_id_attr(self):
        """check State's id attribute is public"""
        state = State()
        self.assertEqual(str, type(state.id))

    def test_State_createAt_attr(self):
        """check State's create_at attribute is public"""
        state = State()
        self.assertEqual(datetime, type(state.created_at))

    def test_State_updatedAt_attr(self):
        """check State's updated_at attribute is public"""
        state = State()
        self.assertEqual(datetime, type(state.updated_at))


    def test_State_two_states_diffrent_ids(self):
        """check two states have diffrent id"""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_State_init_unused_args(self):
        """check that args are not used"""
        obj1 = State("val")
        self.assertNotIn("val", obj1.__dict__.values())

    def test_State_two_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            State().to_dict("val")

class StateSaveTest(unittest.TestCase):
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

    def test_State_save_none_arg(self):
        """test save with None arg"""
        obj1 = State()
        with self.assertRaises(TypeError):
            obj1.save(None)

    def test_State_save_updatedAt_is_date(self):
        """check if save() saves datetime"""
        obj1 = State()
        self.assertEqual(type(obj1.updated_at), datetime)

    def test_State_save_updatedAt_changed(self):
        """check if save() changes the updated_at"""
        obj1 = State()
        oldDate = obj1.updated_at
        obj1.save()
        newDate = obj1.updated_at
        self.assertTrue(oldDate < newDate)

    def test_State_save_file_json(self):
        """test if instance is saved in the json file"""
        obj1 = State()
        obj1.save()
        val = "State." + obj1.id
        with open("file.json", "r") as file:
            self.assertIn(val, file.read())

    def test_State_save_file_json_two_instances(self):
        """test if two instances is saved in the json file"""
        obj1 = State()
        obj2 = State()
        obj1.save()
        sleep(0.05)
        obj2.save()
        val1 = "State." + obj1.id
        val2 = "State." + obj2.id

        with open("file.json", "r") as file:
            self.assertIn(val1, file.read())
        with open("file.json", "r") as file:
            self.assertIn(val2, file.read())


class StateToDictTest(unittest.TestCase):
    """test to_dict()"""
    def test_State_to_dict_vs_dunder_dict(self):
        "check obj.to_dict() is equal to obj.__dict__"
        obj1 = State()
        self.assertNotEqual(obj1.to_dict(), obj1.__dict__)

    def test_State_to_dict_with_arg(self):
        """test save with an arg"""
        obj1 = State()
        with self.assertRaises(TypeError):
            obj1.save("val")

    def test_to_dict_attributes_type_str(self):
        """check if the attributes are strings"""
        obj = State()
        obj_dict = obj.to_dict()
        self.assertEqual(str, type(obj_dict["id"]))
        self.assertEqual(str, type(obj_dict["created_at"]))
        self.assertEqual(str, type(obj_dict["updated_at"]))

    def test_State_initialization_with_kwargs(self):
        """check State when initializated with kwargs"""
        state = State()
        date = datetime.now()
        state.id = "123-456-78"
        state.created_at = state.updated_at = date
        state.name = "NA"
        td = {
            "id": "123-456-78",
            "name": "NA",
            "created_at": date.isoformat(),
            "updated_at": date.isoformat(),
            "__class__": "State"
        }
        self.assertDictEqual(state.to_dict(), td)
