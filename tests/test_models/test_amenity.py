#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from sqlalchemy import inspect
from sqlalchemy.sql import sqltypes

class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
        self.inspector = inspect(Amenity)

    def test_name2(self):
        """ test the type of name """
        info = self.inspector.columns['name']
        new = self.value()
        self.assertEqual(type(info.type), sqltypes.String)
