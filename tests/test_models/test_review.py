#!/usr/bin/python3
""" Unittests for review class """
import unittest
from models.review import Review
from tests.test_models.test_base_model import test_basemodel


class test_review(test_basemodel):
    """ Test class for review """

    def __init__(self, *args, **kwargs):
        """ Test review class instantiation """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test place id type """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test user id type """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Test text type """
        new = self.value()
        self.assertEqual(type(new.text), str)


if __name__ == '__main__':
    unittest.main()
