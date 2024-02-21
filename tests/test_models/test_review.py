#!/usr/bin/python3
"""
Unittest for the Class "Review"
"""

import os
import io
import unittest
import pep8
import inspect
import datetime
import uuid
import models
from unittest.mock import patch
from models.review import Review


class TestReviewDocumentationAndStyle(unittest.TestCase):
    """
    Tests for the Review class documentation and style.
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_funcs = inspect.getmembers(
                Review, predicate=inspect.isfunction
                )

    def test_pep8_conformance_Review(self):
        """
        Test that models/review.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/review.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_Review(self):
        """
        Test that tests/test_models/test_review.py
        conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["tests/test_models/test_review.py"]
        )
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_review_class_docstring(self):
        """
        Test for the Review class docstring
        """
        self.assertIsNot(
                Review.__doc__,
                None,
                "Review class needs a docstring"
                )
        self.assertTrue(
            len(Review.__doc__) >= 1, "Review class needs a docstring"
        )

    def test_review_func_docstrings(self):
        """
        Tests for the presence of docstrings in Review methods
        """
        for func in self.review_funcs:
            self.assertIsNot(
                func[1].__doc__,
                None,
                "{:s} method needs a docstring".format(func[0])
                )
            self.assertTrue(
                len(func[1].__doc__) >= 1,
                "{:s} method needs a docstring".format(func[0]),
                )


class Test_Review(unittest.TestCase):
    '''Test Review class'''
    def test_docstr(self):
        '''Test class documentaion'''
        self.assertTrue(len(Review.__doc__) > 2)

    def test_init(self):
        '''Test instances/cls attrs exists'''
        rev = Review()
        # instance attrs
        self.assertTrue(hasattr(rev, 'id'))
        self.assertTrue(hasattr(rev, 'created_at'))
        self.assertTrue(hasattr(rev, 'updated_at'))
        # cls attrs
        self.assertTrue(hasattr(rev, 'place_id'))
        self.assertTrue(hasattr(rev, 'user_id'))
        self.assertTrue(hasattr(rev, 'text'))

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db',
            "skip if database storage"
            )
    def test_type_attrs(self):
        '''Test instance types'''
        rev = Review()
        # instance attrs
        self.assertIsInstance(rev.id, str)
        self.assertIsInstance(rev.created_at, datetime.datetime)
        self.assertIsInstance(rev.updated_at, datetime.datetime)
        # cls attrs
        self.assertIsInstance(rev.place_id, str)
        self.assertIsInstance(rev.user_id, str)
        self.assertIsInstance(rev.text, str)

    def test_args(self):
        '''Test anonymous arguments'''
        id = str(uuid.uuid4())
        rev = Review(id)
        self.assertNotEqual(id, rev.id)

    def test_kwargs(self):
        '''Test named arguments'''
        kw = {
                'id': 1, 'created_at': datetime.datetime.now(),
                'updated_at': datetime.datetime.now()
             }
        with self.assertRaises(TypeError):
            Review(**kw)
        kw['created_at'] = datetime.datetime.now().isoformat()
        kw['updated_at'] = datetime.datetime.now().isoformat()
        rev = Review(**kw)
        self.assertEqual(rev.id, kw['id'])
        self.assertEqual(rev.created_at.isoformat(), kw['created_at'])
        self.assertEqual(rev.updated_at.isoformat(), kw['updated_at'])

    def test_save(self):
        '''Test saving object to file.json'''
        rev = Review()
        prev_date = rev.updated_at
        rev.save()
        curr_date = rev.updated_at
        self.assertIn('Review'+'.'+rev.id,
                      models.FileStorage._FileStorage__objects)
        self.assertNotEqual(prev_date.isoformat(), curr_date.isoformat())
        with self.assertRaises(TypeError):
            rev.save('')

    def test_to_dict(self):
        '''Test `to_dict` method'''
        rev = Review()
        dct = rev.to_dict()
        self.assertIn('__class__', dct)
        self.assertEqual('Review', dct['__class__'])
        with self.assertRaises(TypeError):
            rev.to_dict({'id': '123'})
            Review()

    def test_str(self):
        '''Test `Review` representaion'''
        with patch('sys.stdout', new_callable=io.StringIO) as m_stdout:
            rev = Review()
            print(rev)
            self.assertEqual(m_stdout.getvalue(),
                             '[Review] ({}) {}\n'.format(rev.id, rev.__dict__))


if __name__ == '__main__':
    unittest.main()
