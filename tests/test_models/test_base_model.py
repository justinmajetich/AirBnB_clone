#!/usr/bin/python3
"""Defines unittests for models/base_model.py

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the class: BaseModel"""

    def test_no_arguments(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_stored(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_public_and_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_public_and_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_public_and_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_ids_two(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_created_different_times(self):
        base1 = BaseModel()
        sleep(0.1)
        base2 = BaseModel()
        self.assertLess(base1.created_at, base2.created_at)

    def test_updated_different_times(self):
        base1 = BaseModel()
        sleep(0.1)
        base2 = BaseModel()
        self.assertLess(base1.updated_at, base2.updated_at)

    def test_instance_args_unuesed(self):
        base1 = BaseModel(None)
        self.assertNotIn(None, base1.__dict__.values())

    def test_kwargs_with_none_value(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_str_rep(self):
        d_t = datetime.now()
        d_t_r = repr(d_t)
        base1 = BaseModel()
        base1.id = "66566"
        base1.created_at = d_t
        base1.updated_at = d_t
        base1_str = base1.__str__()
        self.assertIn("[BaseModel] (66566)", base1_str)
        self.assertIn("'id': '66566'", base1_str)
        self.assertIn("'created_at': " + d_t_r, base1_str)
        self.assertIn("'updated_at': " + d_t_r, base1_str)


class TestBaseModel_save(unittest.TestCase):
    """Unitests for save method of class: BaseModel"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "other")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("other", "file.json")
        except IOError:
            pass

    def test_first_save(self):
        base1 = BaseModel()
        sleep(0.1)
        first_updated = base1.updated_at
        base1.save()
        self.assertLess(first_updated, base1.updated_at)

    def test_second_save(self):
        base1 = BaseModel()
        sleep(0.1)
        first_update = base1.updated_at
        base1.save()
        second_update = base1.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.1)
        base1.save()
        self.assertLess(second_update, base1.updated_at)

    def test_save_with_argument(self):
        base1 = BaseModel()
        with self.assertRaises(TypeError):
            base1.save(None)

    def test_save_updating_file(self):
        base1 = BaseModel()
        base1.save()
        base1id = "BaseModel." + base1.id
        with open("file.json", "r") as file:
            self.assertIn(base1id, file.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unitests for to_dict method of class: BaseModdel"""

    def test_to_dict_type(self):
        base1 = BaseModel()
        self.assertTrue(dict, type(base1.to_dict()))

    def test_to_dict_keys(self):
        base1 = BaseModel()
        self.assertIn("id", base1.to_dict())
        self.assertIn("created_at", base1.to_dict())
        self.assertIn("updated_at", base1.to_dict())
        self.assertIn("__class__", base1.to_dict())

    def test_to_dict_includes_new_attributes(self):
        base1 = BaseModel()
        base1.owner = "Mei"
        base1.score = 100
        self.assertIn("owner", base1.to_dict())
        self.assertIn("score", base1.to_dict())

    def test_to_dict_stores_datetime_as_str(self):
        base1 = BaseModel()
        base1_dict = base1.to_dict()
        self.assertEqual(str, type(base1_dict["created_at"]))
        self.assertEqual(str, type(base1_dict["updated_at"]))

    def test_to_dict_result(self):
        d_t = datetime.now()
        base1 = BaseModel()
        base1.id = "187"
        base1.created_at = d_t
        base1.updated_at = d_t
        base1_dict = {
                "id": "187",
                "__class__": "BaseModel",
                "created_at": d_t.isoformat(),
                "updated_at": d_t.isoformat()
        }
        self.assertDictEqual(base1.to_dict(), base1_dict)

    def test_to_dict_not_dunder_dict(self):
        base1 = BaseModel()
        self.assertNotEqual(base1.to_dict(), base1.__dict__)

    def test_to_dict_with_arguments(self):
        base1 = BaseModel()
        with self.assertRaises(TypeError):
            base1.to_dict(None)


if __name__ == "__main__":
    unittest.main()
