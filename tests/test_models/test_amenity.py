#!/usr/bin/python3
""" Unittest for class Amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Unittest for amenity class"""

    def __init__(self, *args, **kwargs):
        """ test init of class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test type of name attribut"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_to_dict_Amenity(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)
