#!/usr/bin/python3
"""Test Review Class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test review Class"""

    def __init__(self, *args, **kwargs):
        """Test review constructor"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test user id in place"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test text in review"""
        new = self.value()
        self.assertEqual(type(new.text), str)
