#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipIf(True,
                     "state_id needs to be explicitely created unless \
            we are querying the database")
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_state_id(self):
        """ """
        attr = {'state_id': '12346'}
        new = self.value(**attr)
        self.assertEqual(type(new.state_id), str)

    @unittest.skipIf(True,
                     "name needs to be explicitely created unless \
            we are querying the database")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(type(new).__name__), str)

    def test_name(self):
        """ """
        attr = {'name': 'Nairobi'}
        new = self.value(**attr)
        self.assertEqual(type(type(new).__name__), str)
