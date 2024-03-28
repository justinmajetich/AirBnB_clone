#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from sqlalchemy import inspect
from sqlalchemy.sql import sqltypes


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        self.inspector = inspect(Place)
    def test_city_id(self):
        """ """
        new = self.value()
        info = self.inspector.columns['city_id']
        self.assertEqual(type(info.type), sqltypes.String)

    def test_user_id(self):
        """ """
        new = self.value()
        info = self.inspector.columns['user_id']
        self.assertEqual(type(info.type), sqltypes.String)

    def test_name(self):
        """ """
        new = self.value()
        info = self.inspector.columns['name']
        self.assertEqual(type(info.type), sqltypes.String)

    def test_description(self):
        """ """
        new = self.value()
        info = self.inspector.columns['description']
        self.assertEqual(type(info.type), sqltypes.String)

    def test_number_rooms(self):
        """ """
        new = self.value()
        info = self.inspector.columns['rooms']
        self.assertEqual(type(info.type), sqltypes.Integer)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        info = self.inspector.columns['bathrooms']
        self.assertEqual(type(info.type), sqltypes.Integer)

    def test_max_guest(self):
        """ """
        new = self.value()
        info = self.inspector.columns['max_guest']
        self.assertEqual(type(info.type), sqltypes.Integer)

    def test_price_by_night(self):
        """ """
        new = self.value()
        info = self.inspector.columns['price_by_night']
        self.assertEqual(type(info.type), sqltypes.Integer)

    def test_latitude(self):
        """ """
        new = self.value()
        info = self.inspector.columns['latitude']
        self.assertEqual(type(info.type), sqltypes.Float)

    def test_longitude(self):
        """ """
        new = self.value()
        info = self.inspector.columns['longitude']
        self.assertEqual(type(info.type), sqltypes.Float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
