#!/usr/bin/python3
""" unittest module for review """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import pep8
import unittest
import models.review

class test_review(test_basemodel):
    """ test review base model is function"""

    def __init__(self, *args, **kwargs):
        """ instantiates review model for testing"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test proper creation of place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ test proper creation of user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ test proper creation of reveiw text"""
        new = self.value()
        self.assertEqual(type(new.text), str)


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in review class"""

    def test_module_doc(self):
        """ checks for module doc"""
        self.assertGreaterEqual(len(models.review.__doc__), 1)

    def test_class_doc(self):
        """ checks for class doc"""
        self.assertGreaterEqual(len(Review.__doc__), 1)


class TestReviewpep8(unittest.TestCase):
    """ tests review class for pep8 compliance"""

    def test_pep8_compliance(self):
        """ test to ensure models/review.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/review.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """ test to ensure tests/test_models/test_review.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_review.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")