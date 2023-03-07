#!/usr/bin/python3
""" base model test module"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
from uuid import UUID
import json
import os
import pycodestyle


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "Using DB")
class TestBaseModel(unittest.TestCase):
    """ a class for testing the base model """

    @classmethod
    def setUpClass(cls):
        """ Example Data """
        cls.base = BaseModel()
        cls.base.name = "Tabs"
        cls.base.id = "1234"

    @classmethod
    def teardown(cls):
        """ tear down cls """
        del cls.base

    def tearDown(self):
        """ tear down for file storage """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pycodestyle_BaseModel(self):
        """ testing for pycodestyle """
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.new.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.delete.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_BaseModel_methods(self):
        """ Check if Basemodel has methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "new"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "delete"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_BaseModel_type(self):
        """test if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    # BaseModel isn't a part of the DB, so .save() just won't work with it
    # in this context. .save() needs to be a part of file_storage testing
    # def test_BaseModel_save(self):
    #    """ Testing save """
    #    self.base.save()
    #    self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_str(self):
        """ old test for str rep"""
        self.assertEqual(str(self.base),
                         '[{}] ({}) {}'.format(self.base.__class__.__name__,
                                               self.base.id,
                                               self.base.to_dict()))

    def test_to_dict(self):
        """ test for to_dict """
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertEqual(base_dict['created_at'],
                         self.base.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'],
                         self.base.updated_at.isoformat())
        self.assertRaises(KeyError, lambda: base_dict['_sa_instance_state'])