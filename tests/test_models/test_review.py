#!/usr/bin/python3
"""Test Review Class"""
import unittest
import pycodestyle
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReviewDoc(unittest.TestCase):
    """check Review documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(Review.__doc__) > 0)


class TestReviewPycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycodestyle(self):
        """tests pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/review.py']).total_errors,
            0, "PEP 8 style issues found"
        )


class test_review(test_basemodel):
    """Test review Class"""

    def __init__(self, *args, **kwargs):
        """Test review constructor"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test user id in place"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test text in review"""
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_review_inheritance(self):
        """test attributes of review class"""
        self.assertTrue(issubclass(self.value, BaseModel))


if __name__ == "__main__":
    unittest.main()
