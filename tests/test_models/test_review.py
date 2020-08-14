#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from os import getenv


class test_review(test_basemodel):
    """ """

    if getenv("HBNB_TYPE_STORAGE") != "db":

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
    else:
        def test_review_attributes(self):
            """ """
            new = Review(text="nice", place_id="001", user_id="007")
            self.assertEqual(type(new.place_id), str)
            self.assertEqual(type(new.user_id), str)
            self.assertEqual(type(new.text), str)
