#!/usr/bin/python3
"""Unittest module for review"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import pep8
import unittest
import models.review


class test_review(test_basemodel):
    """Tests review base model is functioning"""

    def __init__(self, *args, **kwargs):
        """Instantiates review model for testing"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test proper creation of place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test proper creation of user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test proper creation of review text"""
        new = self.value()
        self.assertEqual(type(new.text), str)


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in review class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.review.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(Review.__doc__), 1)


class TestReviewPep8(unittest.TestCase):
    """Tests Review Class for pep8 compliance"""

    def test_pep8_compliance(self):
        """Tests to ensure models/review.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/review.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Test to ensure tests/test_models/test_review.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_review.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
