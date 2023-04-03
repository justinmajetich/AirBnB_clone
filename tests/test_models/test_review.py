#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest


class test_review(test_basemodel):
    """ """
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.obj = Review()
        cls.obj.text = "Great !"
        cls.obj.place_id = "4534"
        cls.obj.user_id = "543"

    def is_subclass(self):
        """ tests subclass of BaseModel """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)

    def test_place_id(self):
        """ """
        self.assertEqual(type(self.obj.place_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.obj.user_id), str)

    def test_text(self):
        """ """
        self.assertEqual(type(self.obj.text), str)


if __name__ == "__main__":
    unittest.main()
