#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from sqlalchemy.sql import sqltypes
from sqlalchemy import inspect


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
        self.inspector = inspect(City)

    def test_state_id(self):
        """ """
        new = self.value()
        info = self.inspector.columns['state_id']
        self.assertEqual(type(info.type), sqltypes.String)

    def test_name(self):
        """ """
        new = self.value()
        info = self.inspector.columns['name']
        self.assertEqual(type(info.type), sqltypes.String)
