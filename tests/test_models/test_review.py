#!/usr/bin/python3
"""  Tests for review """

import unittest
import models
from models.review import Review
from models.base_model import BaseModel


class review_tests(unittest.TestCase):
    """ Tests for review file """

    def test_reviewsub(self):
        """ Test for the subclass review """
        instance = Review()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_reviewname(self):
        """ Test for the name"""
        instance = Review()
        self.assertTrue(hasattr(instance, "place_id"))
        self.assertEqual(instance.place_id, "")
        self.assertTrue(hasattr(instance, "user_id"))
        self.assertEqual(instance.user_id, "")
        self.assertTrue(hasattr(instance, "text"))
        self.assertEqual(instance.user_id, "")
