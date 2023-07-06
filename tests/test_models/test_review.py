#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
        self.review = self.value()
        self.review.place_id = "0001"
        self.review.user_id = "0002"
        self.review.text = "Awesome Place"

    def test_place_id(self):
        """ """
        self.assertEqual(type(self.review.place_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.review.user_id), str)

    def test_text(self):
        """ """
        self.assertEqual(type(self.review.text), str)
