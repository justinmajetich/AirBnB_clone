#!/usr/bin/python3
"""
test review
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """
    test_review
    """

    def __init__(self, *args, **kwargs):
        """
        __init__
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        test_place_id
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        test_user_id
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        test_text
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
