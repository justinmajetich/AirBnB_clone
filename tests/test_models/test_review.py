#!/usr/bin/python3
""" Unittest test cases for 'models.review' """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest


class test_review(test_basemodel):
    """ Test the instantiation of the Review class. """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.model = Review

    def test_instance_exists(self):
        """ """
        self.assertIsNotNone(self.model)

    def test_class_attributes(self):
        """ """
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))

    def test_class_attributes_type(self):
        """ """
        self.assertIsInstance(getattr(Review, 'place_id'), str)
        self.assertIsInstance(getattr(Review, 'user_id'), str)
        self.assertIsInstance(getattr(Review, 'text'), str)


if __name__ == '__main__':
    unittest.main()
