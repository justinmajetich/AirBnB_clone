#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest


class test_City(test_basemodel):
    """ test for City model """
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.obj = City()
        cls.obj.name = "Toulouse"

    @classmethod
    def tearDown(self):
        """ removes json file """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def is_subclass(self):
        """ test subclass of BaseModel """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)

    def test_name(self):
        """ tests the type """
        new = self.value()
        self.assertEqual(type(self.obj.name), str)


if __name__ == "__main__":
    unittest.main()
