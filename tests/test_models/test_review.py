#!/usr/bin/python3
""" tests for review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest


class test_review(unittest.TestCase,test_basemodel):
    """ class for testing review class"""

    def __init__(self, *args, **kwargs):
        """ initiate the review class"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test place_id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test user_id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ test test_text"""
        new = self.value()
        self.assertEqual(type(new.text), str)
