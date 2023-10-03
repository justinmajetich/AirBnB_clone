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
        new = self.value(place_id="565-5654-45654-45654")
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value(user_id="dfdg-4545-454-gdg")
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value(text="hey you")
        self.assertEqual(type(new.text), str)
