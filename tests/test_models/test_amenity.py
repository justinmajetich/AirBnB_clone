#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest


class test_Amenity(unittest.TestCase):
    """ tests for Amenity class """
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.obj = Amenity()
        cls.obj.name = "Wifi"

    @classmethod
    def tearDown(self):
        """ removes json file """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def type_obj(self):
        """ test type """
        self.assertEqual(type(self.obj.name), str)

    def is_subclass(self):
        """ tests subclass of BaseModel """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)

    def dic_save(self):
        obj = Place()
        obj.name = "Flat"
        place = obj.to_dict
        self.assertTrue(type(place), dict)

"""
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
"""


if __name__ == "__main__":
    unittest.main()
