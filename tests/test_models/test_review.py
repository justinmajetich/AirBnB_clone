#!/usr/bin/python3
"""
script contains unit tests for the Review class
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """
    Test case for the Review class, which inherits from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the test case
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        Test case to verify the type of the place_id attribute
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Test case to verify the type of the user_id attribute
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Test case to verify the type of the text attribute
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
