#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from unittest.mock import patch
import pycodestyle
import models
from uuid import UUID


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8_state(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        """check if state is an instance of BaseModel"""
        state = State()
        self.assertIsInstance(state, State)

    def test_docstrings(self):
        """test documentation"""
        self.assertIsNotNone(State.__doc__)

    def test_type_state(self):
        """Test the type of the attribute"""
        state = State()
        self.assertEqual(type(state.name), str)

    def test_hasattr(self):
        """Test if an object has an attribute"""
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_subclass(self):
        """test if class is subclass"""
        self.assertEqual(issubclass(State, BaseModel), True)

    def test_normal_cases(self):
        """normal cases"""
        obj = State()
        obj.name = "Runspenstinski"
        obj.save()
        obj_dict = obj.to_dict()
        self.assertEqual(obj.name, "Runspenstinski")
        self.assertEqual(obj.__class__.__name__, "State")
        self.assertEqual(isinstance(obj.created_at, datetime), True)
        self.assertEqual(isinstance(obj.updated_at, datetime), True)
        self.assertEqual(type(obj_dict), dict)


class test_inherit_basemodel(unittest.TestCase):
    """Test if user inherit from BaseModel"""
    def test_instance(self):
        """check if Review is an instance of BaseModel"""
        user = State()
        self.assertIsInstance(user, State)
        self.assertTrue(issubclass(type(user), BaseModel))
        self.assertEqual(str(type(user)), "<class 'models.state.State'>")

    """Testing State class"""
    def test_instances(self):
        with patch('models.state'):
            instance = State()
            self.assertEqual(type(instance), State)
            instance.name = "SiliconValley"
            expectec_attrs_types = {
                    "id": str,
                    "created_at": datetime,
                    "updated_at": datetime,
                    "name": str,
                    }
            inst_dict = instance.to_dict()
            expected_dict_attrs = [
                    "id",
                    "created_at",
                    "updated_at",
                    "name",
                    "__class__"
                    ]
            self.assertCountEqual(inst_dict.keys(), expected_dict_attrs)
            self.assertEqual(inst_dict['name'], "SiliconValley")
            self.assertEqual(inst_dict['__class__'], 'State')

            for attr, types in expectec_attrs_types.items():
                with self.subTest(attr=attr, typ=types):
                    self.assertIn(attr, instance.__dict__)
                    self.assertIs(type(instance.__dict__[attr]), types)
            self.assertEqual(instance.name, "SiliconValley")

    def test_State_id_and_createat(self):
        """testing id for every user"""
        user_1 = State()
        sleep(2)
        user_2 = State()
        sleep(2)
        user_3 = State()
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
        inst = State()
        str_output = "[State] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(str_output, str(inst))

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Testing save method and if it update"""
        instance5 = State()
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
