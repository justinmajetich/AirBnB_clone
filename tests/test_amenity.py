#!/usr/bin/python3
""" """
from tests.test_basemodel import test_basemodel
from models.amenity import Amenity

class test_User(test_basemodel):
    """ """


    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
