#!/usr/bin/python3
"""
Test for BaseModel class
"""

from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """
    Definition of tests for the class
    """
    # Set maxDiff to see all output on error comparison
    maxDiff = None

    def __init__(self, *args, **kwargs):
        """
        Initialize the class
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        Set up the method for each test
        """
        pass

    def tearDown(self):
        """
        Tear down method for each test
        """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """
        Ensure default instance creation works
        """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """
        Ensure keyword arguments can be used to create instance of the class
        """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        Ensure that integers can't be passed as keywords
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save_stores(self):
        """
        Ensure that the save method in the class works properly
        """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_save_id(self):
        """
        Ensure that on saving a model, the `updated_at` attribute is
        changed with the current time the object was saved
        """
        new = self.value()
        updated_at = new.updated_at
        # Modify the object
        new.name = 'my_model'
        new.my_number = 89
        # Save the object
        new.save()
        # Ensure that the `updated_at` attribute is updated
        self.assertNotEqual(updated_at, new.updated_at)

    def test_str(self):
        """
        Ensure that the class instances are well represented in string format
        """
        unnecessary_keys = ["_sa_instance_state"]
        i = self.value()

        # Ensure unnecessary keys are not returned in string representation
        for key in str(i):
            with self.subTest(key=key):
                self.assertNotIn(key, unnecessary_keys)

        # Make a new copy of self
        rep = dict()
        for key, value in i.__dict__.items():
            if key in unnecessary_keys:
                continue
            else:
                rep.update({key: value})

        self.assertEqual(str(i), '[{}] ({}) {}'.format(
            self.name, i.id, rep))

    def test_todict(self):
        """
        Ensure that instances of the class can be returned as a dictionary
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_is_different(self):
        """
        Ensure that an object created by kwargs is different from the same
        object created normally using no kwargs
        """
        my_model = self.value()
        my_model.my_number = 89
        my_model.name = "My_first_Model"

        my_model_dict_rep = my_model.to_dict()
        new_model = self.value(**my_model_dict_rep)

        self.assertFalse(my_model is new_model)

    def test_kwargs_none(self):
        """
        Ensure that `None` type can't be used as a keyword argument
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    '''
    def test_kwargs_one(self):
        """
        Ensure that it is impossible to use one kwarg
        """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)
    '''

    def test_kwargs(self):
        """
        Ensure that it is possible to use kwargs to initialize an instance
        """
        kwargs = {"name": "AirBnB clone", "city_id": 32}
        new = self.value(**kwargs)

        self.assertIn("name", new.to_dict())
        self.assertIn("city_id", new.to_dict())

    def test_id(self):
        """
        Ensure that the Identification key is a string
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """
        Ensure that `created_at` attribute is a datetime.datetime
        object
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Ensure that for new instances, created_at and updated_at
        attributes should be the same
        """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        self.assertEqual(new.updated_at, new.created_at)
