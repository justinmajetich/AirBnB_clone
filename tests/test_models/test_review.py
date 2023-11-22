#!/usr/bin/python3
""" """
import unittest
from models.review import Review


class test_review(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_invalid_param(self):
        """test that an invalid parameter is not considered"""
        new = self.value({"invalid_param": "value"})
        self.assertNotIn("invalid_param", new.to_dict())
