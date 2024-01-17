#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_init(self):
        """
        Test the initialization of the BaseModel.
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str(self):
        """
        Test the string representation of the BaseModel.
        """
        my_model = BaseModel()
        my_model_str = str(my_model)
        self.assertTrue("[BaseModel]" in my_model_str)
        self.assertTrue(my_model.id in my_model_str)

    def test_save(self):
        """
        Test the save method of the BaseModel.
        """
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel.
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'],
                         my_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
