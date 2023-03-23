#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Test for the class Review"""

    def __init__(self, *args, **kwargs):
        """ Initialization of the test Review"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ A test to check for the place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ A test to check for he user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ A test to check for the text"""
        new = self.value()
        self.assertEqual(type(new.text), str)
