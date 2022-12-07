#!/usr/bin/python3
""" Unittest for base_model
"""

import unittest
from datetime import datetime
import models
from models.base_model import BaseModel
from os import path
from unittest import mock


class Test_BaseModel(unittest.TestCase):
    """Test different attributes and methods of BaseModel instances
    """

    def setUp(self):
        """set up of the test instance base
        """
        self.base = BaseModel()
        self.base2 = BaseModel()
        self.d = self.base.to_dict()

    def test_attributes(self):
        """test regular attributes
        """
        self.assertNotEqual(self.base.id, self.base2.id)
        self.assertIsInstance(self.base.created_at, datetime)

    @mock.patch('models.storage.save')
    def test_save(self, mock_save):
        """test method save
        """
        old_created_at = self.base.created_at
        old_updated_at = self.base.updated_at
        self.base.save()
        new_created_at = self.base.created_at
        new_updated_at = self.base.updated_at
        self.assertEqual(old_created_at, new_created_at)
        self.assertNotEqual(new_created_at, new_updated_at)
        self.assertNotEqual(old_updated_at, new_updated_at)
        mock_save.assert_called_once()

    def test_to_dict(self):
        """test method to_dict
        """
        self.assertIsInstance(self.d, dict)
        self.assertTrue('__class__' in self.d)
        self.assertIsInstance(self.d['created_at'], str)
        self.assertIsInstance(self.d['updated_at'], str)

    def test__str__(self):
        """test str representation of the instance
        """
        s = f"[{self.base.__class__.__name__}] " \
            f"({self.base.id}) {self.base.__dict__}"
        self.assertEqual(self.base.__str__(), s)

    if __name__ == "__main__":
        unittest.main()
