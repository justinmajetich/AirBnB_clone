#!/usr/bin/python3
"""testing for the db_storage"""
import os
import models
import unittest
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.city import City
import models
@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "only for testing db storage")
class test_DBStorage(unittest.TestCase):
    """testing for the db_storage class"""
    def testCity(self):
        city = City(name="Delhi")
        if city.id in models.storage.all():
            self.assertTrue(city.name, "Delhi")
    def testPlace(self):
        place = Place(name="matchstick apartment", number_rooms=5)
        if place.id in models.storage.all():
            self.assertTrue(place.number_rooms, 5)
            self.assertTrue(place.name, "matchstick apartment")
    def testReview(self):
        review = Review(text="hello")
        if review.id in models.storage.all():
            self.assertTrue(review.text, "Whaddup")
    def testState(self):
        state = State(name="Gregory")
        if state.id in models.storage.all():
            self.assertTrue(state.name, "Gregory")
    def testAmenity(self):
        amenity = Amenity(name="Toilet")
        if amenity.id in models.storage.all():
            self.assertTrue(amenity.name, "Bathtub")
    def testUser(self):
        user = User(name="Hail the lord")
        if user.id in models.storage.all():
            self.assertTrue(user.name, "Hail the lord")
    def teardown(self):
        self.session.close()
        self.session.rollback()
