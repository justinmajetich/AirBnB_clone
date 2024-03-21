#!/usr/bin/python3
"""
Test Case For City Model
"""
from models.base_model import BaseModel
from models.city import City
import unittest
from datetime import datetime
import json
import os


class TestCity(unittest.TestCase):
    """
    Test cases for City class
    """

    def setUp(self):
        """Set up testing environment"""
        self.test_instance = City()

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """Test instance creation and type"""
        self.assertIsInstance(self.test_instance, City)

    def test_attributes(self):
        """Test instance attributes"""
        self.assertTrue(hasattr(self.test_instance, 'id'))
        self.assertTrue(hasattr(self.test_instance, 'created_at'))
        self.assertTrue(hasattr(self.test_instance, 'updated_at'))
        self.assertTrue(hasattr(self.test_instance, 'name'))
        self.assertTrue(hasattr(self.test_instance, 'state_id'))

    def test_id_type(self):
        """Test type of id attribute"""
        self.assertIsInstance(self.test_instance.id, str)

    def test_created_at_type(self):
        """Test type of created_at attribute"""
        self.assertIsInstance(self.test_instance.created_at, datetime)

    def test_updated_at_type(self):
        """Test type of updated_at attribute"""
        self.assertIsInstance(self.test_instance.updated_at, datetime)

    def test_name_type(self):
        """Test type of name attribute"""
        self.assertIsInstance(self.test_instance.name, str)

    def test_state_id_type(self):
        """Test type of state_id attribute"""
        self.assertIsInstance(self.test_instance.state_id, str)

    def test_str_method(self):
        """Test __str__ method"""
        expected_str = "[City] ({}) {}".format(self.test_instance.id,
                                               self.test_instance.__dict__)
        self.assertEqual(str(self.test_instance), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        expected_dict = {
            '__class__': 'City',
            'id': self.test_instance.id,
            'created_at': self.test_instance.created_at.isoformat(),
            'updated_at': self.test_instance.updated_at.isoformat(),
            'name': self.test_instance.name,
            'state_id': self.test_instance.state_id
        }
        self.assertDictEqual(self.test_instance.to_dict(), expected_dict)

    def test_save_method(self):
        """Test save method"""
        self.test_instance.save()
        self.assertIsInstance(self.test_instance.updated_at, datetime)

    def test_save_to_json(self):
        """Test that save method saves to file"""
        self.test_instance.save()
        with open('file.json', 'r') as f:
            obj_dict = json.load(f)
            key = "City." + self.test_instance.id
            self.assertIn(key, obj_dict)

    def test_save_updates_json(self):
        """Test that save method updates file"""
        self.test_instance.save()
        with open('file.json', 'r') as f:
            obj_dict = json.load(f)
            key = "City." + self.test_instance.id
            self.assertEqual(obj_dict[key], self.test_instance.to_dict())

    def test_init_with_kwargs(self):
        """Test instance creation with kwargs"""
        new_instance = City(id="123", created_at="2023-01-01T00:00:00",
                            updated_at="2023-01-01T00:00:00",
                            name="test", state_id="123")
        self.assertEqual(new_instance.id, "123")
        self.assertEqual(new_instance.created_at.isoformat(), "2023-01-01T00:00:00")
        self.assertEqual(new_instance.updated_at.isoformat(), "2023-01-01T00:00:00")
        self.assertEqual(new_instance.name, "test")
        self.assertEqual(new_instance.state_id, "123")

    def test_invalid_kwargs(self):
        """Test instance creation with invalid kwargs"""
        with self.assertRaises(TypeError):
            new_instance = City(invalid_key="value")

    def test_different_instances_have_different_ids(self):
        """Test that different instances have different ids"""
        instance1 = City()
        instance2 = City()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_updated_at_times(self):
        """Test that created_at and updated_at times are equal when created"""
        instance = City()
        self.assertEqual(instance.created_at, instance.updated_at)

    def test_updated_at_changes_on_save(self):
        """Test that updated_at changes on save"""
        instance = City()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_reload_method(self):
        """Test reload method"""
        instance = City()
        instance.save()
        instance_id = instance.id
        del instance
        new_instance = City()
        models.storage.reload()
        loaded_instance = models.storage.all()["City." + instance_id]
        self.assertEqual(new_instance.id, loaded_instance.id)
        self.assertEqual(new_instance.created_at, loaded_instance.created_at)
        self.assertEqual(new_instance.updated_at, loaded_instance.updated_at)

