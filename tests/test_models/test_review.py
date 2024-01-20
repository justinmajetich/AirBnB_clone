#!/usr/bin/python3
"""
Test for Review class.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for Review class.
    """

    def test_attributes(self):
        """
        Test Review attributes.
        """
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, None)
        self.assertEqual(review.user_id, None)
        self.assertEqual(review.text, None)


if __name__ == '__main__':
    unittest.main()
