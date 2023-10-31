#!/usr/bin/python3
"""Unittest file for testing place class """
import models
from os import getenv
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.city import City
from models.user import User
from models.state import State

class TestPlace(test_basemodel):
    """ Unit testing for place class"""

    def __init__(self, *args, **kwargs):
        """ inicialization values """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        self.state = State(name="Colorado")
        self.city = City(name="Denver", state_id=self.state.id)
        self.user = User(name="Chico", email="chicoguey@realgmail.com")
        self.place = Place(
            user_id=self.user.id, city_id=self.city.id, name="Mountain Cabin",
            number_rooms=3, number_bathrooms=2, max_guest=4,
            price_by_night=100)
        
if __name__ == "__main__":
    unittest.main()