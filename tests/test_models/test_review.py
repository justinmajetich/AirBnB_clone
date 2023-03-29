#!/usr/bin/python3
""" module for.review reviews"""
import unittest
import pycodestyle
from models.review import Review
from models.base_model import BaseModel
import os


class TestReview(unittest.TestCase):
    """ a class for testing Review"""

    @classmethod
    def setUpClass(cls):
        """ Example Data """
        cls.rev = Review()
        cls.rev.place_id = "gilded-lily"
        cls.rev.user_id = "johnny-sinner"
        cls.rev.text = "Best Damn Flowers this side of San Francisco"

    def teardown(cls):
        """ tear down Class """
        del cls.rev

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_Review_pycodestyle(self):
        """check for pycodestyle """
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(["models/review.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_Review_docs(self):
        """ check for docstring """
        self.assertIsNotNone(Review.__doc__)

    def test_Review_attribute_types(self):
        """ test Review attribute types """
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)
        self.assertEqual(type(self.rev.text), str)

    def test_Review_is_subclass(self):
        """ test if Review is subclass of BaseModel """
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "Review won't\
                     save because it needs to be tied to a user :\\")
    def test_Review_save(self):
        """ test save() command """
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_Review_sa_instance_state(self):
        """ test is _sa_instance_state has been removed """
        self.assertNotIn('_sa_instance_state', self.rev.to_dict())


if __name__ == "__main__":
    unittest.main()