#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from models.state import State

from models.user import User


class test_fileStorage(unittest.TestCase):
    """Class to test the file storage method"""

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def setUp(self):
        """Set up test environment"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def tearDown(self):
        """Remove storage file at end of tests"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_obj_list_empty(self):
        """__objects is initially empty"""
        self.assertEqual(len(storage.all()), 0)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_new(self):
        """New object is correctly added to __objects"""
        new = BaseModel()
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_all(self):
        """__objects is properly returned"""
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_all_with_class(self):
        """__objects is properly returned with a class filter"""
        new = BaseModel().save()
        new = BaseModel().save()
        new = User().save()
        new = BaseModel().save()
        new = State().save()
        temp = storage.all("BaseModel")
        self.assertIsInstance(temp, dict)
        self.assertEqual(len(temp), 3)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_all_invalid_class(self):
        """__objects is properly returned with am invalid class filter"""
        BaseModel()
        BaseModel()
        User()
        BaseModel()
        State()
        temp = storage.all("Invalid")
        self.assertIsInstance(temp, dict)
        self.assertTrue(len(temp) == 0)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_base_model_instantiation(self):
        """File is not created on BaseModel save"""
        new = BaseModel()
        self.assertFalse(os.path.exists("file.json"))

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_empty(self):
        """Data is saved to file"""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize("file.json"), 0)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_save(self):
        """FileStorage save method"""
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_delete(self):
        """FileStorage delete method"""
        new = BaseModel()
        storage.delete(new)
        key = "".format(new.__class__, new.id)
        self.assertTrue(key not in storage.all().keys())

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_delete_invalid_cls_no_id(self):
        """FileStorage delete method with a dummy class with no id"""

        class Dummy:
            pass

        new = Dummy()
        self.assertRaises(
            AttributeError, lambda: storage.delete(new)  # anonymous func :)
        )

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_delete_invalid_cls(self):
        """FileStorage delete method"""

        class Dummy:
            id = "thisisanid"
            pass

        new = Dummy()
        prev = storage.all()
        storage.delete(new)
        next = storage.all()

        self.assertTrue(len(prev) == len(next))

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_delete_none(self):
        """FileStorage delete method"""
        new = BaseModel()
        new2 = BaseModel()
        new3 = BaseModel()
        all = storage.all()
        storage.delete(None)
        self.assertTrue(all == storage.all())

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_reload(self):
        """Storage file is successfully loaded to __objects"""
        new = BaseModel()
        new.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()["id"], loaded.to_dict()["id"])

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_reload_empty(self):
        """Load from an empty file"""
        with open("file.json", "w") as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_reload_from_nonexistent(self):
        """Nothing happens if file does not exist"""
        self.assertEqual(storage.reload(), None)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_base_model_save(self):
        """BaseModel save method calls storage save"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists("file.json"))

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_type_path(self):
        """Confirm __file_path is string"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_type_objects(self):
        """Confirm __objects is a dict"""
        self.assertEqual(type(storage.all()), dict)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_key_format(self):
        """Key is properly formatted"""
        new = BaseModel()
        _id = new.to_dict()["id"]
        new.save()
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, "BaseModel" + "." + _id)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not db",
    )
    def test_storage_var_created(self):
        """FileStorage object storage created"""
        from models.engine.file_storage import FileStorage

        self.assertEqual(type(storage), FileStorage)
