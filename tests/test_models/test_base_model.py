#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8


class test_basemodel(unittest.TestCase):
    """Class test using unittest"""

    @classmethod
    def setUpClass(cls):
        cls.prueba = BaseModel()
        cls.prueba.name = "team"
        cls.prueba.age = 25

    @classmethod
    def tearDown(cls):
        del cls.prueba

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_documentation(self):
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_args_kwargs(self):
        self.assertEqual(self.prueba.name, "team")
        self.assertEqual(self.prueba.age, 25)
        self.assertTrue(hasattr(self.prueba, "name"))
        self.assertTrue(hasattr(self.prueba, "age"))

    def test_BaseModel(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__str__"))

    def test_save(self):
        self.prueba.save()
        self.assertNotEqual(self.prueba.created_at, self.prueba.updated_at)

    def test_to_dict(self):
        self.assertEqual(self.prueba.__class__.__name__, "BaseModel")
        b = self.prueba.to_dict()
        self.assertIsInstance(b['created_at'], str)

    def test_str(self):
        bstr = self.prueba.__str__()
        self.assertEqual(bstr, "[BaseModel] ({}) {}".format(
            self.prueba.id, self.prueba.__dict__))


if __name__ == "__main__":
    unittest.main()
