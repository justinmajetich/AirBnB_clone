#!/usr/bin/python3
""" test module for Review class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from test_models import storage_type


class test_review(test_basemodel):
    """ Test suite for `Review` class """

    def __init__(self, *args, **kwargs):
        """ initialize attributes """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test place id """
        new = self.value()
        self.assertEqual(type(new.place_id),
                         str if storage_type != "db" else type(None))

    def test_user_id(self):
        """ test user_id """
        new = self.value()
        self.assertEqual(type(new.user_id),
                         str if storage_type != "db" else type(None))

    def test_text(self):
        """ test_text """
        new = self.value()
        self.assertEqual(type(new.text),
                         str if storage_type != "db" else type(None))
