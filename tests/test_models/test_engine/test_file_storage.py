#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def test_save(self):
        """ Testing if the file is created """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_empty(self):
        """ Testing empty file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertEqual(os.path.getsize('file.json'), 10238)
