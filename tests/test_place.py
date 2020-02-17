#!/usr/bin/python3
""" """
from tests.test_basemodel import test_basemodel
from models.place import Place

class test_User(test_basemodel):
    """ """


    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
