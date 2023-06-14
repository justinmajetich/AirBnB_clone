#!/usr/bin/python3
"""
This module defines all extra tests for the Review model
"""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """
    Define tests for the class Review
    """

    def __init__(self, *args, **kwargs):
        """
        Intialize the class
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    '''
    # TESTS NO LONGER REQUIRED
    def test_place_id(self):
        """
        Ensure that the attribute `place_id` is a string
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Ensure that the attribute `user_id` is a string
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Ensure that the attribute `text` is a string
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
    '''
