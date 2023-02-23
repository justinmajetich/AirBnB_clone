#!/usr/bin/python3

import inspect
import json
import os
import unittest
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine import db_storage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import pycodestyle

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Skip if not database")
class TestDBStorage(unittest.TestCase):
    """Tests for database storage"""

def setUp(self):
    """Set up for tests """
    self.storage = models.storage

def tearDown(self):
    """Delete storage after tests"""
    del self.storage

def test_user(self):
    """user test"""
    test_user = User(name="Jessica")
    test_user.save()
    self.assertTrue(test_user.id in self.storage.all())
    self.assertEqual(test_user.name, "Jessica")

def test_city(self):
    """Test for city"""
    test_city = City(name="Abuja")
    test_state = State()
    test_city.state_id = test_state.id
    test_city.save()
    self.assertTrue(test_city.id in self.storage.all())
    self.assertEqual(test_city.name, "Abuja")

def test_state(self):
    """Test for state"""
    test_state = State(name="California")
    test_state.save()
    self.assertTrue(test_state.id in self.storage.all())
    self.assertEqual(test_state.name, "California")

def test_place(self):
    """Test for place"""
    test_place = Place(name="Garki", number_rooms=2)
    test_place.save()
    self.assertTrue(test_place.id in self.storage.all())
    self.assertEqual(test_place.number_rooms, 4)
    self.assertEqual(test_place.name, "Garki")

def test_amenity(self):
    """Test for amenity"""
    test_amenity = Amenity(name="Washing Machine")
    test_amenity.save()
    self.assertTrue(test_amenity.id in self.storage.all())
    self.assertEqual(test_amenity.name, "Washing Machine")

def test_review(self):
    """Test for review"""
    test_review = Review(text="Awesome Place")
    test_review.save()
    self.assertTrue(test_review.id in self.storage.all())
    self.assertEqual(test_review.text, "Awesome Place")
