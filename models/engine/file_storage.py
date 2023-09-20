#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:43:09 2020
@author: meco
"""
import os
import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
from contextlib import redirect_stdout
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User


class FileStorage(unittest.TestCase):
    """
    class for testing FileStorage class' methods
    """
    temp_file = ""

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_FileStorage(self):
        """
        Test that file_storage.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/file_storage.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_FileStorage(self):
        """
        Test that test_file_storage.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/\
                                        test_file_storage.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    @staticmethod
    def test_move_file(src, dest):
        with open(src, 'r', encoding='utf-8') as myFile:
            with open(dest, 'w', encoding='utf-8') as tempFile:
                tempFile.write(myFile.read())
        os.remove(src)

    def setUp(self):
        self.temp_file = '/temp_store.json'
        self.temp_objs = [BaseModel(), BaseModel(), BaseModel()]
        for obj in self.temp_objs:
            storage.new(obj)
        storage.save()

    def tearDown(self):
        """initialized object
        """
        del self.temp_objs

    def test_type(self):
        """type checks for FileStorage
        """
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(type(storage), FileStorage)

    def test_save(self):
        """tests save functionality for FileStorage
        """
        with open('file.json', 'r', encoding='utf-8') as myFile:
            dump = myFile.read()
        self.assertNotEqual(len(dump), 0)
        temp_d = eval(dump)
        key = self.temp_objs[0].__class__.__name__ + '.'
        key += str(self.temp_objs[0].id)
        self.assertNotEqual(len(temp_d[key]), 0)
        key2 = 'State.412409120491902491209491024'
        try:
            self.assertRaises(temp_d[key2], KeyError)
        except:
            pass

    def test_reload(self):
        """tests reload functionality for FileStorage
        """
        storage.reload()
        obj_d = storage.all()
        key = self.temp_objs[1].__class__.__name__ + '.'
        key += str(self.temp_objs[1].id)
        self.assertNotEqual(obj_d[key], None)
        self.assertEqual(obj_d[key].id, self.temp_objs[1].id)
        key2 = 'State.412409120491902491209491024'
        try:
            self.assertRaises(obj_d[key2], KeyError)
        except:
            pass

    def test_delete_basic(self):
        """tests delete basic functionality for FileStorage
        """
        obj_d = storage.all()
        key2 = self.temp_objs[2].__class__.__name__ + '.'
        key2 += str(self.temp_objs[2].id)
        try:
            self.assertRaises(obj_d[key2], KeyError)
        except:
            pass

    def test_new_basic(self):
        """tests new basic functionality for FileStorage
        """
        obj = BaseModel()
        storage.new(obj)
        obj_d = storage.all()
        key = obj.__class__.__name__ + '.' + str(obj.id)
        self.assertEqual(obj_d[key] is obj, True)

    def test_new_badinput(self):
        """tests new bad input functionality for FileStorage
        """
        try:
            self.assertRaises(storage.new('jwljfef'), TypeError)
            self.assertRaises(storage.new(None), TypeError)
        except:
            pass