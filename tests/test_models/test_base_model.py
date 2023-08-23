#!/usr/bin/python3
""" Test for BaseModel"""
from models.base_model import BaseModel
import unittest
import pep8
import os


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Test setup"""
        cls.base = BaseModel()
        cls.base.name = "Yan"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """test Tear down"""
        del cls.base

    def tearDown(self):
        """Tear down method"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/base_model.py'])
        self.assertEqual(res.total_errors, 0, "fix pep8")

    def test_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """chekcing if Basemodel have certain methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """test if the base is of type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_BaesModel(self):
        """test if BaseModel save method"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        """test BaseModel to_dict method"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
