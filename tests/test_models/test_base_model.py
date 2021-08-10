#!/usr/bin/python3
"""
    Test Case For Base Model and its Test
"""
from models.base_model import BaseModel
import unittest
import inspect
import time
from datetime import datetime
import pep8 as pcs
from unittest import mock
import models
base_doc = BaseModel.__doc__


class TestDocBaseModule(unittest.TestCase):
    """
        Base module Documentaion and pep8 Test
    """
    @classmethod
    def setUpClass(cls):
        """
            Setting Up Class for test
        """
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def pep8_test_base(self):
        """
            Test pep8 for base module
        """
        path = "models/base_model.py"
        with self.subTest(path=path):
            Error = pcs.Checker(path).check_all()
            self.assertEqual(Error, 0)

    def pep8_test_testbase(self):
        """
            Test pep8 for Unitesst base module
        """
        path = 'tests/test_models/test_base_model.py'
        with self.subTest(path=path):
            Error = pcs.Checker(path).check_all()
            self.assertEqual(Error, 0)

    def test_doc_base(self):
        """
            Test Documantaion for Base model
        """
        self.assertIsNot(base_doc, None, "Doc missing")
        self.assertTrue(len(BaseModel.__doc__) >= 1, "Doc Missing")
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__, None,
                    "Documentaion missing in base model"
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "Documentaion missiing in base model")


class TestBaseModel(unittest.TestCase):
    """
        Test Case For Base Model
    """
    @mock.patch('models.storage')
    def Test_instance(self, mock_storage):
        """
            Testing Base Model Class
        """
        instance = BaseModel()
        self.assetrtIs(type(instance), BaseModel)
        instance.name = "Ahmed"
        instance.phone = 9525
        type_attr = {
            "id": str,
            "updated_at": datetime,
            "created_at": datetime,
            "name": str,
            "phone": int
        }
        for attr, type_at in type_attr.items():
            with self.subTest(attr=attr, typ=type_at):
                self.assertIn(attr, instance.__dict__)
                self.assertIs(type(instance.__dict__[attr]), type_at)
            self.assertTrue(mock_storage.new_called)
            self.assertEqual(instance.name, "Ahmed")
            self.assertEqual(instance.phone, 9525)

    def Test_datetime(self):
        """
        Test diffrent instance  diffrent time
        test Same created at and updated when
        instance is Created
        """
        tc_before = datetime.now()
        instance1 = BaseModel()
        tc_after = datetime.now()
        self.assertTrue(tc_before <= instance1.created_at <= tc_after)
        time.sleep(1e-4)
        instance2 = BaseModel()
        self.assertEqual(instance1.created_at, instance1.updated_at)
        self.assertNotEqual(instance1.created_at, instance2.created_at)
        self.assertNotEqual(instance1.updated_at, instance2.updated_at)

    def test_uiid(self):
        """
            Test Diffrent uiid diffrent instance
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)
        uuid = instance1.id
        with self.subTest(uuid=uuid):
            self.assertIs(type(uuid), str)

    def test_to_dict(self):
        """
            test to dic method in base model
        """
        instance = BaseModel()
        instance.name = "ahmed"
        instance.num = 95
        dict_inst = instance.to_dict()
        attribute = [
            "id",
            "created_at",
            "updated_at",
            "name",
            "num",
            "__class__"]
        self.assertCountEqual(dict_inst.keys(), attribute)
        self.assertEqual(dict_inst['__class__'], 'BaseModel')
        self.assertEqual(dict_inst['name'], "ahmed")
        self.assertEqual(dict_inst['num'], 95)

    def to_dict_value(self):
        """
            test that to dict return are correct or no
        """
        time_f = "%Y-%m-%dT%H:%M:%S.%f"
        instance = BaseModel()
        dict_base = instance.to_dict()
        self.assertEqual(dict_base["__class__"], "BaseModel")
        self.assertEqual(type(dict_base["created_at"]), str)
        self.assertEqual(type(dict_base["updated_at"]), str)
        self.assertEqual(
            dict_base["created_at"],
            instance.created_at.strftime(time_f)
        )
        self.assertEqual(
            dict_base["updated_at"],
            instance.updated_at.strftime(time_f)
        )

    @mock.patch("models.storage")
    def test_save(self, mock_storage):
        """
            test save and update at is working and storage call
            save
        """
        instance = BaseModel()
        old_value_created = instance.created_at
        old_value_update = instance.updated_at
        instance.save()
        new_value_created = instance.created_at
        new_value_updated = instance.updated_at
        self.assertNotEqual(old_value_update, new_value_updated)
        self.assertEqual(old_value_created, new_value_created)
        self.assertTrue(mock_storage.save.called)