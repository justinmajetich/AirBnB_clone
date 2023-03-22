#!/usr/bin/python3
""" """
from models.amenity import Amenity
import unittest


class test_Amenity(unittest.TestCase):
    """ """

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
        self.assertEqual(type(self.obj.name), str)

    def is_subclass(self):
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)
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