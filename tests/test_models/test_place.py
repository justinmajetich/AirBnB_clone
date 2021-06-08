#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.city import City
from models.user import User
from models.state import State
import os

new_C = City(name='City_1', state_id=State(name='Oregon').id)
new_U = User(email="john69@hotmail.com", password="4201337",
             first_name="John", last_name="Hancock")
new = Place(city_id=new_C.id, user_id=new_U.id, name='KFC',
            description='Fried', number_rooms=2,
            number_bathrooms=1, max_guest=30,
            price_by_night=5, latitude=1.2, logitude=3.4)


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        self.assertEqual(type(new.latitude), float)
