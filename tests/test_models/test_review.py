#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models import BaseModel


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id_value(self):
        """Test place_id value of Review"""
        new = self.value()
        new.place_id = "1234"
        self.assertEqual(new.place_id, "1234")

    def test_user_id_value(self):
        """Test user_id value of Review"""
        new = self.value()
        new.user_id = "5678"
        self.assertEqual(new.user_id, "5678")

    def test_text_value(self):
        """Test text value of Review"""
        new = self.value()
        new.text = "Test review"
        self.assertEqual(new.text, "Test review")

    def test_update_text(self):
        """Test update_text method of Review"""
        new = self.value()
        new.text = "Initial review"
        new.update_text("Updated review")
        self.assertEqual(new.text, "Updated review")

    def test_inheritance(self):
        """Test that Review correctly inherits from BaseModel"""
        new = self.value()
        self.assertIsInstance(new, BaseModel)

    def test_place_id_type(self):
        """Test place_id type error handling of Review"""
        new = self.value()
        with self.assertRaises(TypeError):
            new.place_id = 1234  # Attempt to set place_id to an integer
