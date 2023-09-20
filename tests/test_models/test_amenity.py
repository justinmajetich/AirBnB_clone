#!/usr/bin/python3
""" Tests for the amenity class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest


class test_Amenity(unittest.TestCase,test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ initializes test_amenity class"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
    
    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
    
