#!/usr/bin/python3
'''
    Testing the file_storage module.
'''

import os
import time
import json
import sys
import io
import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
from console import HBNBCommand


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "test only for FileStorage")
class testFileStorage(unittest.TestCase):
    '''
        Testing the FileStorage class
    '''

    def setUp(self):
        '''
            Initializing classes
        '''
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        '''
            Cleaning up.
        '''
        pass
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_return_type(self):
        '''
            Tests the data type of the return value of the all method.
        '''
        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_new_method(self):
        '''
            Tests that the new method sets the right key and value pair
            in the FileStorage.__object attribute
        '''
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_objects_value_type(self):
        '''
            Tests that the type of value contained in the FileStorage.__object
            is of type obj.__class__.__name__
        '''
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        val = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.my_model, type(val))

    def test_save_file_exists(self):
        '''
            Tests that a file gets created with the name file.json
        '''
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_read(self):
        '''
            Testing the contents of the files inside the file.json
        '''
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = json.load(fd)

        self.assertTrue(type(content) is dict)

    def test_the_type_file_content(self):
        '''
            testing the type of the contents inside the file.
        '''
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = fd.read()

        self.assertIsInstance(content, str)

    def test_reaload_without_file(self):
        '''
            Tests that nothing happens when file.json does not exists
            and reload is called
        '''

        try:
            self.storage.reload()
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_parameter_validity(self):
        '''
            Tests whether or not the parameter passed is an instance of the
            class
        '''
        console = HBNBCommand()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        my_id = console.onecmd("create State name='California'")
        sys.stdout = sys.__stdout__
        with open("file.json", encoding="UTF-8") as fd:
            json_dict = json.load(fd)
        for key, value in json_dict.items():
            my_key = 'State.' + str(my_id)
            if key == my_key:
                self.assertTrue(value['name'] == 'California')

    def test_parameter_lack_of_validity(self):
        '''
            Tests whether or not the parameter passes is an instance
            of the class
        '''
        console = HBNBCommand()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        my_id = console.onecmd("create State address=98")
        sys.stdout = sys.__stdout__
        self.assertIsNone(my_id)

    def test_deletion(self):
        '''
            Tests for an object being deleted with the delete method
        '''
        fs = FileStorage()
        new_state = State()
        new_state.name = "Polynesia"
        fs.new(new_state)
        my_id = new_state.id
        fs.save()
        fs.delete(new_state)
        with open("file.json", encoding="UTF-8") as fd:
            json_dict = json.load(fd)
        for key, value in json_dict.items():
            self.assertTrue(value['id'] != my_id)
