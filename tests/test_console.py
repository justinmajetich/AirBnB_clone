#!/usr/bin/python3

import unittest
from console import HBNBCommand
from models.__init__ import storage

import os

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cli = HBNBCommand()

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_do_create(self):
        # Test creating a new instance
        
        #get number of items before storage
        old_objs = len(storage.all())
        self.cli.onecmd('create Place city_id=1')
        all_objs = len(storage.all())
        self.assertEqual(all_objs, old_objs + 1)

    def test_do_create_integer(self):
        """Test creating  an item with integer attribute"""
        new_obj = self.cli.onecmd('create Place city_id=1')
        self.assertEqual(new_obj.city_id, 1)
        # print(storage.all()) 
        # self.assertEqual(storage.all()['Place.id'].city_id, 1)
    def test_do_create_float(self):
        # Test creating a new instance with float attribute

        new_obj = self.cli.onecmd('create User latitude=2.2')
        self.assertEqual(new_obj.latitude, 2.2)


    def test_do_create_string(self):
        # Test creating a new instance with string attribute

        new_obj = self.cli.onecmd('create State name="Entebbe"')
        self.assertEqual(new_obj.name, "Entebbe")

        # self.assertEqual(storage.all()['Place'].name, 'Entebbe')

        # Test creating a new instance with string attribute containing spaces
        # self.cli.onecmd('create City name="Cape_Town"')
        # all_objs = storage.all()
        # for key, val in all_objs.items():
        #     if 'City' in key:
        #         self.assertEqual(val.name, "Cape Town")
        # self.assertEqual(storage.all()['Place'].name, 'Cape Town')

