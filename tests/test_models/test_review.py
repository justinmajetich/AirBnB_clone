#!/usr/bin/python
"""Unittest for Review class """
from os import getenv
import models
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from sqlalchemy.exc import OperationalError

class TestReview(test_basemodel):
    """ Unit test class for testing review class """


    def setUp(self):
        """ Initilization of review instance """
        super().setUp()
        self.name = "Review"
        self.value = Review
        self.state = State(name="Michigan")
        self.city = City(name="Lancing", state_id=self.state.id)
        self.user = User(name="Jacob_Morgan", email="jmorgan1124@gmail.com")
        self.place = Place(
            user_id=self.user.id, city_id=self.city.id, name="Lofty_Lookout",
            number_rooms=5, number_bathrooms=3, max_guest=8,
            price_by_night=215)
        self.review = Review(place_id=self.place.id, text="Amazing View!",
                             user_id=self.user.id)
        
if __name__ == "__main__":
    unittest.main()   