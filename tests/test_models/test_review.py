#!/usr/bin/python3
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


class test_review(test_basemodel):
    """Unittest for Review class """

    def __init__(self, *args, **kwargs):
        """Instantiation """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
        self.state = State(name="Florida")
        self.city = City(name="Miami", state_id=self.state.id)
        self.user = User(name="Oscar_the_father", email="the_father@yahoo.com")
        self.place = Place(
            user_id=self.user.id, city_id=self.city.id, name="San_Luis",
            number_rooms=6, number_bathrooms=4, max_guest=5,
            price_by_night=230)
        self.review = Review(place_id=self.place.id, text="Awesome Place",
                             user_id=self.user.id)

    def test_place_id(self):
        """ test place id in review class"""
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(self.review.place_id, self.place.id)

    def test_user_id(self):
        """ test user id in review class"""
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(self.review.user_id, self.user.id)

    def test_text(self):
        """ test to check the text in review class"""
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(self.review.text, "Awesome Place")

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "not supported")
    def test_without_mandatory_arguments(self):
        """Check """
        new = self.value()
        with self.assertRaises(OperationalError):
            try:
                new.save()
            except Exception as error:
                models.storage._DBStorage__session.rollback()
                raise error

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "not supported")
    def test_is_subclass(self):
        """Check that Review is a subclass of Basemodel"""
        self.assertTrue(isinstance(self.review, Review))
