#!/usr/bin/env python3
"""
A unit test module for testing ``models/base_model.py`` module.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """
    Test the basic features of the BaseModel class.
    """

    def test_instance_uuid_is_unique(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_instance_created_at_is_str(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        base1 = BaseModel()
        self.assertEqual(type(base1.created_at), datetime)

    def test_instance_updated_at_is_str(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        base1 = BaseModel()
        self.assertEqual(type(base1.updated_at), datetime)

    def test_save_method(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        from time import sleep
        base1 = BaseModel()
        sleep(2)
        base1.save()
        self.assertNotEqual(base1.created_at, base1.updated_at)

    def test_BaseModel_save_method(self):
        """
        This method tests save method of the class
        BaseModel.
        """
        BaseModel().save()

    def test_string_representation(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        base1 = BaseModel()
        string = "[{}] ({}) {}".format(base1.__class__.__name__,
                                       base1.id, base1.__dict__)
        self.assertEqual(base1.__str__(), string)

    def test_instance_dictionary(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        base1 = BaseModel()
        base1.name = "New Instance variable"
        self.assertTrue("__class__" in base1.to_dict())
        self.assertTrue("id" in base1.to_dict())
        self.assertTrue("created_at" in base1.to_dict())
        self.assertTrue("updated_at" in base1.to_dict())
        self.assertTrue("name" in base1.to_dict())

    def test_new_instance_from_dictionary(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        base1 = BaseModel()
        model_json = base1.to_dict()
        base2 = BaseModel(**model_json)
        self.assertFalse(base1 is base2)

    def test_new_instance_datetime_variables(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        base1 = BaseModel()
        model_json = base1.to_dict()
        base2 = BaseModel(**model_json)
        self.assertEqual(type(base2.created_at), datetime)
        self.assertEqual(type(base2.updated_at), datetime)

    def test_new_instance_properties_against_old(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        base1 = BaseModel()
        base1.name = "New_Instance"
        model_json = base1.to_dict()
        base2 = BaseModel(**model_json)
        self.assertEqual(type(base1), type(base2))
        self.assertEqual(base1.id, base2.id)
        self.assertEqual(base1.created_at, base2.created_at)
        self.assertEqual(base1.updated_at, base2.updated_at)
        self.assertEqual(base1.name, base2.name)
