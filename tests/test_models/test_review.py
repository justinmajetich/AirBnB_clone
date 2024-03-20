#!/usr/bin/python3
"""Unit tests for the Review class."""

# Importing necessary modules
from tests.test_models.test_base_model import test_basemodel
from models.review import Review

class TestReviewAttributes(test_basemodel):
    """Test cases for the attributes of the Review class."""
    
    def __init__(self, *args, **kwargs):
        """Initialize test cases."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id_type(self):
        """Test if the 'place_id' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id_type(self):
        """Test if the 'user_id' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text_type(self):
        """Test if the 'text' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.text), str)
