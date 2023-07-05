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

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual((new.place_id), None)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual((new.user_id), None)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual((new.text), None)