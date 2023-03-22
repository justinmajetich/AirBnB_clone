#!/usr/bin/python3

import unittest
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "only testing db storage")
class test_DBStorage(unittest.TestCase):

    def testState(self):
        state = State(name="Greg")
        if state.id in models.storage.all():
            self.assertTrue(state.name, "Greg")

    def testCity(self):
        city = City(name="Afa")
        if city.id in models.storage.all():
            self.assertTrue(city.name, "Afa")

    def testPlace(self):
        place = Place(name="MyShoeBox", number_rooms=5)
        if place.id in models.storage.all():
            self.assertTrue(place.number_rooms, 5)
            self.assertTrue(place.name, "MyShoeBox")

    def testUser(self):
        user = User(name="Young_Jeezy")
        if user.id in models.storage.all():
            self.assertTrue(user.name, "Young_Jeezy")

    def testAmenity(self):
        amenity = Amenity(name="Toilet")
        if amenity.id in models.storage.all():
            self.assertTrue(amenity.name, "Toilet")

    def testReview(self):
        review = Review(text="hello")
        if review.id in models.storage.all():
            self.assertTrue(review.text, "hello")

    def teardown(self):
        self.session.close()
        self.session.rollback()
