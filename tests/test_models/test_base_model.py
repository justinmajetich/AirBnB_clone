#!/usr/bin/python3
"""
Defines unittests for BaseModel class.
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'test DBStorage only')
class TestBaseModel(unittest.TestCase):
    """Unittests for BaseModel class."""

    def setUp(self):
        """Sets up testing environment."""
        self.bm = BaseModel()

    def tearDown(self):
        """Tears down testing environment."""
        del self.bm

    def test_attributes(self):
        """Tests for expected attributes."""
        self.assertTrue(hasattr(self.bm, 'id'))
        self.assertTrue(hasattr(self.bm, 'created_at'))
        self.assertTrue(hasattr(self.bm, 'updated_at'))

    def test_id(self):
        """Tests for id attribute."""
        self.assertIsInstance(self.bm.id, str)
        self.assertNotEqual(self.bm.id, '')

    def test_created_at(self):
        """Tests for created_at attribute."""
        self.assertIsInstance(self.bm.created_at, datetime.datetime)

    def test_updated_at(self):
        """Tests for updated_at attribute."""
        self.assertIsInstance(self.bm.updated_at, datetime.datetime)

    def test_str(self):
        """Tests __str__ method."""
        expected = "[BaseModel] ({}) {}".format(self.bm.id, self.bm.__dict__)
        self.assertEqual(expected, str(self.bm))

    def test_save(self):
        """Tests save method."""
        old_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(old_updated_at, self.bm.updated_at)

    def test_to_dict(self):
        """Tests to_dict method."""
        expected = {
            'id': self.bm.id,
            'created_at': self.bm.created_at.isoformat(),
            'updated_at': self.bm.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(expected, self.bm.to_dict())

    def test_create_kwargs(self):
        """Tests creating instance with kwargs."""
        bm1 = BaseModel(id='123', created_at='2022-01-01T00:00:00.000000',
                        updated_at='2022-01-01T00:00:00.000000')
        self.assertEqual('123', bm1.id)
        self.assertEqual('2022-01-01T00:00:00', bm1.created_at.strftime('%Y-%m-%dT%H:%M:%S'))
        self.assertEqual('2022-01-01T00:00:00', bm1.updated_at.strftime('%Y-%m-%dT%H:%M:%S'))

    def test_create_empty_dict(self):
        """Tests creating instance with empty dictionary."""
        bm1 = BaseModel({})
        self.assertEqual(str(bm1), "[BaseModel] ({}) {}".format(bm1.id, bm1.__dict__))

    def test_create_new_dict(self):
        """Tests creating instance with new dictionary."""
        bm1 = BaseModel({'name': 'Test'})
        self.assertEqual('Test', bm1.name)

    def test_create_wrong_kwargs(self):
        """Tests creating instance with wrong kwargs."""
        with self.assertRaises(TypeError):
            BaseModel({'name': 'Test', 'id': '123', 'created_at': '2022-01-01T00:00:00.000000',
                       'updated_at': '2022-01-01T00:00:00.000000'})