#!/usr/bin/python3
""" """
from .test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        new.state_id = '0001'
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        new.name = 'City'
        self.assertEqual(type(new.name), str)
