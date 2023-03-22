#!/usr/bin/python3
'''
    Tests for db_storage module
'''
import os
import json
import unittest
import pep8
import models
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from datetime import datetime
from models.engine import db_storage
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'not db storage')
class TestDBStorage(unittest.TestCase):
    '''
    Tests to check the documentation and style of DBStorage class
    '''

    def test_pep8_conformance_db_storage(self):
        '''
        Test that db_storage.py conforms to PEP8.
        '''
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0, "Pep8 Errors")

    def test_db_storage_module_docstring(self):
        '''
        Test for the db_storage.py module docstring
        '''
        self.assertIsNot(db_storage.__doc__, None, "Missing docstring")

    def test_db_storage_class_docstring(self):
        '''
        Test for the DBStorage class docstring
        '''
        self.assertIsNot(DBStorage.__doc__, None, "Missing docstring")

    def test_dbs_func_docstrings(self):
        '''
        Test for docstrings in DBStorage methods
        '''
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_State(self):
        '''
            Tests State class
        '''
        state = State(name='California')
        if state.id in models.storage.all():
            self.assertTrue(state.name, "California")

    def test_City(self):
        '''
            Tests City class
        '''
        city = City(name='San Francisco')
        if city.id in models.storage.all():
            self.assertTrue(city.name, 'San Francisco')

    def test_User(self):
        '''
            Tests User class
        '''
        new_user = User(
            email='boop@boop.com',
            password='boopword',
            first_name='boop',
            last_name='poob')

        self.assertIsInstance(new_user.email, str)
        self.assertIsInstance(new_user.password, str)
        self.assertIsInstance(new_user.first_name, str)
        self.assertIsInstance(new_user.last_name, str)

        self.assertEqual(new_user.password, 'boopword')
        self.assertEqual(new_user.first_name, 'boop')
        self.assertEqual(new_user.last_name, 'poob')

    def testPlace(self):
        '''
        Tests Place class
        '''
        place = Place(name="Home")
        if place.id in models.storage.all():
            self.assertTrue(place.name, "Home")

    def testAmenity(self):
        '''
        Tests Amenity class
        '''
        amenity = Amenity(name='sink')
        if amenity.id in models.storage.all():
            self.assertTrue(amenity.name, 'sink')

    def testReview(self):
        '''
        Test Review class
        '''
        review = Review(text='Nice place')
        if review.id in models.storage.all():
            self.assertTrue(review.text, 'Nice place')

    def teardown(self):
        self.session.close()
        self.session.rollback()
