#!/usr/bin/python3
"""
Here is define some test of console behavior
"""

from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import unittest
from models import storage


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_do_create_having_doc(self):
        self.assertTrue(HBNBCommand.do_create.__doc__ != "")

    def test_do_create_without_class_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.do_create('')
            self.assertEqual("** class name missing **\n", output.getvalue())

    def test_do_create_without_wrong_class_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.do_create('Bonjour')
            self.assertEqual("** class doesn't exist **\n", output.getvalue())

    def test_do_create_with_good_class_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.do_create('State')
            test = storage.all().get(f"State.{output.getvalue()[0:-1]}", False)
            self.assertTrue(test)

    def test_do_create_with_one_good_params(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.do_create('State name="California"')
            data = storage.all().get(f"State.{output.getvalue()[0:-1]}", False)
            self.assertTrue(data)
            self.assertEqual("California", data.name)

    def test_do_create_with_multiple_good_params(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.do_create('Place city_id="0001"\
                user_id="0001" name="My_little_house"\
                number_rooms=4 number_bathrooms=2 max_guest=10\
                price_by_night=300 latitude=37.773972\
                longitude=-122.431297')

            data = storage.all().get(f"Place.{output.getvalue()[0:-1]}", False)
            self.assertTrue(data)
            self.assertEqual("0001", data.city_id)
            self.assertEqual("0001", data.user_id)
            self.assertEqual("My little house", data.name)
            self.assertEqual(4, data.number_rooms)
            self.assertEqual(2, data.number_bathrooms)
            self.assertEqual(10, data.max_guest)
            self.assertEqual(300, data.price_by_night)
            self.assertEqual(37.773972, data.latitude)
            self.assertEqual(-122.431297, data.longitude)

    def test_do_create_with_string(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.do_create('Place city_id="000_1"\
                user_id="0001" name="My\"little_house"')

            data = storage.all().get(f"Place.{output.getvalue()[0:-1]}", False)
            self.assertTrue(data)
            self.assertEqual("000 1", data.city_id)
            self.assertEqual("0001", data.user_id)
            self.assertEqual('My"little house', data.name)
