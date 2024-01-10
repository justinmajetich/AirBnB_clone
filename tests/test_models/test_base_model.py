#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not File",
    )
    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not File",
    )
    def test_default(self):
        i = self.value()
        self.assertEqual(type(i), self.value)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not File",
    )
    def test_kwargs(self):
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not File",
    )
    def test_kwargs_int(self):
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not File",
    )
    def test_save(self):
        """Testing save"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open("file.json", "r") as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not File",
    )
    def test_str(self):
        i = self.value()
        self.assertEqual(
            str(i),
            "[{}] ({}) {}".format(
                self.name,
                i.id,
                {
                    k: v
                    for k, v in i.__dict__.items()
                    if k != "_sa_instance_state"},
            ),
        )

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not File",
    )
    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not File",
    )
    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)
    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not File",
    )
    def test_kwargs_one(self):
        """ """
        n = {"Name": "test"}
        with self.assertRaises(KeyError):
            new = self.value(**n)"""

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not File",
    )
    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not File",
    )
    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "Storage Type is not File",
    )
    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
