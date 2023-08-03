#!/usr/bin/python3
"""
test case test review
"""

import os
import unittest
from models.base_model import BaseModel
from models.review import Review


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "test only for FileStorage")
class TestReview(unittest.TestCase):
    """test case"""

    def test_Review_inheritance(self):
        """
        tests that the Review class
        Inherits from BaseModel
        """
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_Review_attributes(self):
        """
        Test that Review class has place_id, user_id and text
        attributes.
        """
        new_review = Review()
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())

    def test_Review_attributes(self):
        """
        Test that Review class has place_id, user_id and text
        attributes.
        """
        new_review = Review(place_id="dojndnniodw13244", user_id="kwndw71902", text="dojndnniodw13244")
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text = getattr(new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
