#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import os
from models import storage
from models.state import State
from models.city import City


class test_dbStorage(unittest.TestCase):
    """Class to test the file storage method"""

    def setUp(self):
        """Set up test environment"""

        storage.reload()

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_all_env_set(self):
        HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")
        HBNB_ENV = os.getenv("HBNB_ENV")
        HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")

        self.assertEqual(HBNB_MYSQL_HOST, "localhost")
        self.assertEqual(HBNB_MYSQL_PWD, "hbnb_test_pwd")
        self.assertEqual(HBNB_MYSQL_USER, "hbnb_test")
        self.assertEqual(HBNB_MYSQL_DB, "hbnb_test_db")
        self.assertEqual(HBNB_ENV, "test")
        self.assertEqual(HBNB_TYPE_STORAGE, "db")

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_storage_var_created(self):
        """DBStorage object storage created"""
        from models.engine.db_storage import DBStorage

        self.assertEqual(type(storage), DBStorage)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_db_is_dropped(self):
        """db is initially empty"""
        self.assertEqual(len(storage.all()), 0)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_new(self):
        """New object is correctly added to db"""
        new = State()
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_all(self):
        """__objects is properly returned"""
        new = State()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_all_with_class(self):
        """__objects is properly returned with a class filter"""
        new = State().save()
        new = City().save()
        new = City().save()
        new = State().save()
        new = State().save()
        temp = storage.all("State")
        self.assertIsInstance(temp, dict)
        self.assertEqual(len(temp), 3)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_all_invalid_class(self):
        """__objects is properly returned with am invalid class filter"""
        State()
        State()
        State()
        State()
        temp = storage.all("Invalid")
        self.assertIsInstance(temp, dict)
        self.assertTrue(len(temp) == 0)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_save(self):
        """DBStorage save method"""
        new = State()
        res = storage.save()
        self.assertTrue(res is None)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_delete(self):
        """DBStorage delete method"""
        new = State()
        storage.delete(new)
        key = "".format(new.__class__, new.id)
        self.assertTrue(key not in storage.all().keys())

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_delete_invalid_cls_no_id(self):
        """DBStorage delete method with a dummy class with no id"""

        class Dummy:
            pass

        new = Dummy()
        self.assertRaises(
            AttributeError, lambda: storage.delete(new)  # anonymous :)
        )

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_delete_invalid_cls(self):
        """DBStorage delete method"""

        class Dummy:
            id = "thisisanid"
            pass

        new = Dummy()
        prev = storage.all()
        storage.delete(new)
        next = storage.all()

        self.assertTrue(len(prev) == len(next))

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_delete_none(self):
        """DBStorage delete method"""
        new = State()
        new2 = State()
        new3 = State()
        all = storage.all()
        storage.delete(None)
        self.assertTrue(all == storage.all())

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_reload(self):
        """Storage file is successfully loaded to __objects"""
        new = State()
        new.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()["id"], loaded.to_dict()["id"])

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_base_model_save(self):
        """State save method calls storage save"""
        new = State()
        new.save()
        self.assertTrue(os.path.exists("file.json"))

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_type_objects(self):
        """Confirm __objects is a dict"""
        self.assertEqual(type(storage.all()), dict)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") != "db",
        "Storage Type is not db",
    )
    def test_key_format(self):
        """Key is properly formatted"""
        new = State()
        _id = new.to_dict()["id"]
        new.save()
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, "State" + "." + _id)
