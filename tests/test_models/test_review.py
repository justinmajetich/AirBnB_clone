#!/usr/bin/python3
"""
module to test the Review class
"""
import unittest
import os
from models.review import Review


class TestReview(unittest.TestCase):
    """
    test review
    """

    def setUp(self):
        """setUp"""
        if not os.path.exists("file.json"):
            os.mknod("file.json")
        self.review = Review()

    def tearDown(self):
        """tearDown"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        del self.review

    def test_creation(self):
        '''
        ensures correct creaion
        '''
        self.assertEqual(self.review.text, '')
        self.assertEqual(self.review.place_id, '')
        self.assertEqual(self.review.user_id, '')

    def test_types(self):
        '''
        ensure types
        '''
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

    def test_invalid_attributes(self):
        '''
        Test invalid attributes
        '''
        self.review = Review({'ratings': 20, 'username': 'betty'})
        self.assertFalse(hasattr(self.review, 'rating'))
        self.assertFalse(hasattr(self.review, 'username'))
