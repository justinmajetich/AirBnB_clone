#!/usr/bin/python3

import unittest
from console import HBNBCommand
from models.__init__ import storage

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cli = HBNBCommand()

    def test_do_create(self):
        # Test creating a new instance with integer attribute
        self.cli.onecmd('create Place city_id=1')
        all_objs = storage.all()
        for key, val in all_objs.items():
            if 'Place' in key:
                self.assertEqual(val.city_id, 1)
        # print(storage.all()) 
        # self.assertEqual(storage.all()['Place.id'].city_id, 1)

        # Test creating a new instance with float attribute
        self.cli.onecmd('create User latitude=2.2')
        all_objs = storage.all()
        for key, val in all_objs.items():
            if 'User' in key:
                self.assertEqual(val.latitude, 2.2)

        # Test creating a new instance with string attribute
        self.cli.onecmd('create State name="Entebbe"')
        all_objs = storage.all()
        for key, val in all_objs.items():
            if 'State' in key:
                self.assertEqual(val.name, "Entebbe")
        # self.assertEqual(storage.all()['Place'].name, 'Entebbe')

        # Test creating a new instance with string attribute containing spaces
        # self.cli.onecmd('create City name="Cape_Town"')
        # all_objs = storage.all()
        # for key, val in all_objs.items():
        #     if 'City' in key:
        #         self.assertEqual(val.name, "Cape Town")
        # self.assertEqual(storage.all()['Place'].name, 'Cape Town')

