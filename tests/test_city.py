#!/usr/bin/python3
""" """
from tests.test_basemodel import test_basemodel
from models.city import City 

class test_User(test_basemodel):
    """ """


    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City" 
        self.value = City
