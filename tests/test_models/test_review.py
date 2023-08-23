#!/usr/bin/python3
""" """
import os
import unittest
import pep8
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the Review class"""

    @classmethod
    def setUpClass(cls):
        """Test set up"""
        cls.rev = Review()
        cls.rev.place_id = "1234-abcd"
        cls.rev.user_id = "5678-efgh"
        cls.rev.text = "I love it, huge kicthen"

    @classmethod
    def teardown(cls):
        """Test tear down"""
        del cls.rev

    def tearDown(self):
        """Teardown method"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pep8(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/review.py'])
        self.assertEqual(res.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Checking class docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attributes(self):
        """Checking class attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)

    def test_attribute_types(self):
        """Test review attributes Types"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save(self):
        """Test review save method"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict(self):
        """Test rev to_dict method"""
        self.assertEqual('to_dict' in dir(self.rev), True)


if __name__ == '__main__':
    unittest.main()
