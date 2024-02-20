#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.review import Review
import unittest
import os
import pep8


class TestReview(unittest.TestCase):
    """Tests the Review class"""

    @classmethod
    def setUpClass(cls):
        """Creates a review instance"""

        cls.review = Review()
        cls.review.text = 'It was a wonderful stay.'
        cls.review.place_id = "8a6s54d3fg"
        cls.review.user_id = "84s6a5d1f2"

    @classmethod
    def tearDownClass(cls):
        """Delete the review instance"""

        del cls.review

    def tearDown(self):
        """Removes file.json"""

        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attribute_existence(self):
        """Tests for attribute existence in Review class"""

        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)

    def test_attribute_type(self):
        """Tests type of attribute"""

        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db',
                     'Database storage is being used')
    def test_save(self):
        """Tests save method"""

        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        """tests to_dict method"""

        dict = self.review.to_dict()

        self.assertIsInstance(dict['created_at'], str)
        self.assertIsInstance(dict['updated_at'], str)
        self.assertEqual('to_dict' in dir(self.review), True)

    def test_issubclass(self):
        """Tests if Review is subclass of Basemodel"""

        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_documentation(self):
        """Tests if the class is documented"""

        self.assertIsNotNone(Review.__doc__)

    def test_following_pep8(self):
        """Tests if the code follows pep8 style guide"""

        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/review.py'])

        self.assertEqual(result.total_errors, 0, 'Found style errors.')


if __name__ == "__main__":
    unittest.main()
