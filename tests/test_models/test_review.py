#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review
from models.user import User


class test_review(TestBaseModel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test the place_id attribute of the Review class"""
        new = Review()
        new.place_id = "test_place_id"
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test that user_id is a string """
        new_user = User(email="john@example.com", password="password")
        new_user.save()
        new_review = Review(place_id="123", user_id=new_user.id,
                            text="Test review")
        new_review.save()
        self.assertEqual(type(new_review.user_id), str)

    def test_text(self):
        """Test the text attribute of the Review class"""
        new = self.value()
        if new.text is None:
            new.text = ''
        self.assertIsInstance(new.text, str)
        self.assertEqual(new.text, '')

    def test_created_at(self):
        """Test the created_at attribute of the Review class"""
        new = self.value()
        self.assertEqual(type(new.created_at), type(datetime.datetime.now()))

    def test_updated_at(self):
        """Test the updated_at attribute of the Review class"""
        new = self.value()
        self.assertEqual(type(new.updated_at), type(datetime.datetime.now()))