#!/usr/bin/python3
"""
Test module for the Review class using unittest
"""
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class test_review(TestBaseModel):
    """
    subClass of unittest class to test the Review class
    """

    def __init__(self, *args, **kwargs):
        """ Init the reveiw test class and its super"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test the palce_id attribute"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test the user_id attribute"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Test the text attribute"""
        new = self.value()
        self.assertEqual(type(new.text), str)
