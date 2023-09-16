#!/usr/bin/env python3
""" Test cases for base_model
"""
import unittest
import inspect
import os
import uuid
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """BaseModel test cases"""
# --Doc section-----------------------------------
    def test_BaseModule_doc(self):
        """check the module's doc"""
        doc = BaseModel.__doc__
        self.assertTrue(len(doc) > 1)

    def test_BaseModel_str_doc(self):
        """check __str__ doc"""
        doc = BaseModel.__str__.__doc__
        self.assertTrue(len(doc) > 1)

    def test_BaseModel_save_doc(self):
        """check save doc"""
        doc = BaseModel.save.__doc__
        self.assertTrue(len(doc) > 1)

    def test_BaseModel_to_dict_doc(self):
        """check to_dict doc"""
        doc = BaseModel.to_dict.__doc__
        self.assertTrue(len(doc) > 1)

# --Public attribute id-----------------------------
    def test_BaseModel_id_not_null(self):
        """check if id is null"""
        obj = BaseModel()
        self.assertNotEqual(obj.id, None)

    def test_BaseModel_id_is_string(self):
        """check if id is a string"""
        obj1 = BaseModel()
        self.assertTrue(type(obj1.id), str)

    def test_BaseModel_id_is_uuid(self):
        """check if id is a UUID """
        obj = BaseModel()
        self.assertTrue(uuid.UUID(obj.id))

    def test_BaseModel_ids_not_equal(self):
        """check if id is not null"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

# --Public attribute created_at-----------------------------
    def test_BaseModel_createdAt_not_null(self):
        """check if created_at is null"""
        obj1 = BaseModel()
        self.assertNotEqual(obj1.created_at, None)

    def test_BaseModel_createdAt_is_datetime(self):
        """check if created_at is datetime"""
        obj1 = BaseModel()
        self.assertTrue(type(obj1.created_at), datetime)

    def test_BaseModel_createdAt_is_diffrent(self):
        """check that created_at keeps increasing"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertTrue(obj1.created_at < obj2.created_at)

# --Public attribute updated_at-----------------------------
    def test_BaseModel_updatedAt_not_null(self):
        """check if updated_at is null"""
        obj1 = BaseModel()
        self.assertNotEqual(obj1.updated_at, None)

    def test_BaseModel_updatedAt_is_datetime(self):
        """check if updatedd_at is datetime"""
        obj1 = BaseModel()
        self.assertTrue(type(obj1.updated_at), datetime)

# --Object initialization ------------------------------
    def test_BaseModel_init_with_args_no_kwargs(self):
        """check that __dict__ remains unchanged with args provided"""
        obj1 = BaseModel("arg1", "arg2")
        dictLen = len(obj1.__dict__)
        self.assertEqual(dictLen, 3)

    def test_BaseModel_init_unused_args(self):
        """check that args are not used"""
        obj1 = BaseModel("val")
        self.assertNotIn("val", obj1.__dict__.values())

    def test_BaseModel_init_with_args_one_Kwargs(self):
        """check that kwarg has been added"""
        obj1 = BaseModel("arg1", "arg2", name="john")
        dictLen = len(obj1.__dict__)
        self.assertEqual(dictLen, 4)
        self.assertEqual(obj1.__dict__["name"], "john")

    def test_BaseModel_init_with_args_multiple_Kwargs(self):
        """check that kwargs have been added"""
        obj1 = BaseModel("arg1", "arg2", name="john", lastname="doe")
        dictLen = len(obj1.__dict__)
        self.assertEqual(dictLen, 5)
        self.assertEqual(obj1.__dict__["name"], "john")
        self.assertEqual(obj1.__dict__["lastname"], "doe")

    def test_BaseModel_init_with_class_Kwarg(self):
        """check that __class__ is not added"""
        obj1 = BaseModel(__class__=str)
        dictLen = len(obj1.__dict__)
        self.assertEqual(dictLen, 3)

    def test_BaseModel_init_with_Kwarg(self):
        """check that __class__ is not added"""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        _id = "2023"
        obj1 = BaseModel(id=_id, created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(obj1.created_at, dt)
        self.assertEqual(obj1.updated_at, dt)
        self.assertEqual(obj1.id, "2023")


# -- method save() -----------------------------
class BaseModelSaveTest(unittest.TestCase):
    """test cases for BaseModel.save() method"""

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

    def test_BaseModel_save_none_arg(self):
        """test save with None arg"""
        obj1 = BaseModel()
        with self.assertRaises(TypeError):
            obj1.save(None)

    def test_BaseModel_save_updatedAt_is_date(self):
        """check if save() saves datetime"""
        obj1 = BaseModel()
        self.assertEqual(type(obj1.updated_at), datetime)

    def test_BaseModel_save_updatedAt_changed(self):
        """check if save() changes the updated_at"""
        obj1 = BaseModel()
        oldDate = obj1.updated_at
        obj1.save()
        newDate = obj1.updated_at
        self.assertNotEqual(oldDate, newDate)

    def test_BaseModel_save_updatedAt_is_newer(self):
        """check new saved update_at is greater than the old"""
        obj1 = BaseModel()
        oldDate = obj1.updated_at
        obj1.save()
        newDate = obj1.updated_at
        self.assertTrue(oldDate < newDate)

    def test_BaseModel_save_file_json(self):
        """test if instance is saved in the json file"""
        obj1 = BaseModel()
        obj1.save()
        val = "BaseModel." + obj1.id
        with open("file.json", "r") as file:
            self.assertIn(val, file.read())

    def test_BaseModel_save_file_json_two_instances(self):
        """test if two instances is saved in the json file"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        sleep(0.05)
        obj2.save()
        val1 = "BaseModel." + obj1.id
        val2 = "BaseModel." + obj2.id
        with open("file.json", "r") as file:
            self.assertIn(val1, file.read())
        with open("file.json", "r") as file:
            self.assertIn(val2, file.read())


# --method to_dict() -----------------------------
class BaseModelToDictTest(unittest.TestCase):
    """test cases for BaseModel.to_dict() method"""
    def test_BaseModel_to_dict_args(self):
        """to_dict with an arg"""
        obj1 = BaseModel()
        with self.assertRaises(TypeError):
            obj1.to_dict("val")

    def test_BaseModel_to_dict_no_kwargs(self):
        """to_dict with no kwargs"""
        obj1 = BaseModel()
        my_dict = obj1.to_dict()
        self.assertEqual(len(my_dict), 4)
        self.assertEqual(obj1.updated_at.isoformat(), my_dict["updated_at"])
        self.assertEqual(obj1.created_at.isoformat(), my_dict["created_at"])
        self.assertEqual(obj1.id, my_dict["id"])

    def test_BaseModel_to_dict_one_kwarg(self):
        """to_dict with one kwarg"""
        obj1 = BaseModel(name="john", age=30, car=None)
        my_dict = obj1.to_dict()
        self.assertEqual(len(my_dict), 7)
        self.assertEqual(obj1.name, my_dict["name"])
        self.assertEqual(obj1.age, my_dict["age"])
        self.assertEqual(obj1.car, my_dict["car"])

    def test_BaseModel_to_dict_compare(self):
        """compare to_dict"""
        obj1 = BaseModel()
        date = datetime.now()
        obj1.id = "123-456-78"
        obj1.created_at = obj1.updated_at = date
        test_dict = {
            "id": "123-456-78",
            "__class__": "BaseModel",
            "created_at": date.isoformat(),
            "updated_at": date.isoformat()
        }
        self.assertDictEqual(obj1.to_dict(), test_dict)
