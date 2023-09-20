#!/usr/bin/python3
"""This tests for Review class"""
import unittest
import os
import pep8
from os import getenv
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """This tests for the class Review that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """This initializes the test class process """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    @classmethod
    def setUpClass(cls):
        """ This sets up for test"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "The strongest in the Galaxy"

    @classmethod
    def teardown(cls):
        """This will tear setup down  at the end of the test"""
        del cls.rev

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests the pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Review(self):
        """This tests for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """Checks if review have attributes properly set"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_Review(self):
        """Tests if review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_place_id(self):
        """Tests for the attribute place_id of the class Review """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """This tests ifattribute user_id of the class Review works"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Tests if the attribute text of the class Review works """
        new = self.value()
        self.assertEqual(type(new.text), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_Review(self):
        """Tests if the save works"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """Tests if dictionary is working"""
        self.assertEqual('to_dict' in dir(self.rev), True)


if __name__ == "__main__":
    unittest.main()
