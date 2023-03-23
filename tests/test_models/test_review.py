#!/usr/bin/python3
""" Unittest for class Review"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Unittest for class Review"""

    def __init__(self, *args, **kwargs):
        """ test of initialisation class"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test of place_id type attribute """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """  test of user_id type attribute"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ test of text type attribute"""
        new = self.value()
        self.assertEqual(type(new.text), str)
