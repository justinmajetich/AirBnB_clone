#!/usr/bin/python3
"""
File: test_console.py
Author: Teddy Deberdt
Date: 2024-03-25
Description: Tests for HBNB console improvements.
"""
from models.engine.file_storage import FileStorage
from unittest.mock import patch, MagicMock
from console import HBNBCommand
from io import StringIO
import unittest


class TestDoCreate(unittest.TestCase):

    def setUp(self):
        """Setup before each test."""
        self.mock_stdout = patch('sys.stdout', new_callable=StringIO)
        self.mock_storage_new = patch('models.storage.new', MagicMock())
        self.mock_storage_save = patch('models.storage.save', MagicMock())

    def tearDown(self):
        """Cleanup after each test."""
        patch.stopall()

    def test_create_missing_class_name(self):
        """Test reaction to missing class name."""
        with self.mock_stdout as mocked_out:
            HBNBCommand().do_create('')
            self.assertEqual("** class name missing **\n",
                             mocked_out.getvalue())

    def test_create_class_does_not_exist(self):
        """Test reaction to invalid class name."""
        with self.mock_stdout as mocked_out:
            HBNBCommand().do_create('NonExistentClass')
            self.assertEqual("** class doesn't exist **\n",
                             mocked_out.getvalue())

    def test_create_attribute_format_error(self):
        """Test reaction to malformed attribute format."""
        with self.mock_stdout as mocked_out:
            HBNBCommand().do_create('User email="user@example.com" Password')
            self.assertIn(
                "** attribute format error **: Password (expected key=value)",
                mocked_out.getvalue())

    def test_create_with_valid_attributes(self):
        """Test creation with valid attributes."""
        with self.mock_stdout as mocked_out, self.mock_storage_new, \
                self.mock_storage_save:
            HBNBCommand().do_create(
                'Place city_id="0001" user_id="0001" '
                'name="My_little_house" number_rooms=4 number_bathrooms=2 '
                'max_guest=10 price_by_night=300 latitude=37.773972 '
                'longitude=-122.431297')
            self.assertTrue(self.mock_storage_new.called)
            self.assertTrue(self.mock_storage_save.called)

    def test_create_with_mixed_types_attributes(self):
        """Test creation with mixed types attributes."""
        with self.mock_stdout as mocked_out, self.mock_storage_new, \
                self.mock_storage_save:
            HBNBCommand().do_create(
                'Place name="My_little_house" number_rooms=4 '
                'latitude=37.773972 longitude=-122.431297')
            self.assertTrue(self.mock_storage_new.called)
            self.assertTrue(self.mock_storage_save.called)

    def test_create_with_complex_string_attributes(self):
        """Test creation with complex string attributes."""
        with self.mock_stdout as mocked_out, self.mock_storage_new, \
                self.mock_storage_save:
            HBNBCommand().do_create('Place name="\\\"My little house\\\""')
            self.assertTrue(self.mock_storage_new.called)
            self.assertTrue(self.mock_storage_save.called)

    def test_create_with_incomplete_attributes(self):
        """Test creation with incomplete attribute specifications."""
        with self.mock_stdout as mocked_out:
            HBNBCommand().do_create('User email=')
            self.assertIn("** attribute format error **",
                          mocked_out.getvalue())

    def test_create_with_invalid_attribute_format(self):
        """Test reaction to invalid attribute format."""
        with self.mock_stdout as mocked_out:
            HBNBCommand().do_create('User email=user@example.com')
            self.assertIn("** attribute format error **: email=user@example.com (expected key=value)",
                          mocked_out.getvalue())

    def test_create_with_special_characters_in_attribute_values(self):
        """Test creation with special characters in attribute values."""
        with self.mock_stdout as mocked_out, self.mock_storage_new, \
                self.mock_storage_save:
            HBNBCommand().do_create('User password="p@ssw0rd"')
            self.assertTrue(self.mock_storage_new.called)
            self.assertTrue(self.mock_storage_save.called)


if __name__ == "__main__":
    unittest.main()
