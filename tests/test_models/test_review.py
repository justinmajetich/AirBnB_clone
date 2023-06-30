#!/usr/bin/python3
""" """
from models.place import Place
from models.user import User
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """Test for review """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        place = Place()
        new.place_id = place.id
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        user = User()
        new.user_id = user.id
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        new.text = ""
        self.assertEqual(type(new.text), str)
