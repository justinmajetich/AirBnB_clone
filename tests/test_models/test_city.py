#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
        self.city = self.value()
        self.city.name = "San Francisco"
        self.city.state_id = "0001"

    def test_city_id(self):
        """ """
        self.assertEqual(type(self.city.state_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.city.name), str)
