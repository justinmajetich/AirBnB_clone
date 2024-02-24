#!/usr/bin/python3
"""Tests the command interpreter (console.py)"""
import unittest
from console import HBNBCommand
from models import storage
import os


class TestCreateCommand(unittest.TestCase):
    """Tests the create command"""
    def setUp(self):
        """Sets up resources for testing"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Cleans up resources after testing"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_create_with_int_param(self):
        """Tests create command with integer parameter"""
        self.console.do_create("Place number_rooms=3 max_guest=4")
        all_objs = storage.all().values()

        # Fetch the last object created
        obj = max(all_objs, key=lambda x: x.created_at)
        self.assertEqual(obj.number_rooms, 3)
        self.assertEqual(obj.max_guest, 4)

    def test_create_with_float_param(self):
        """Test create command with float parameter"""
        self.console.do_create("Place lat=37.773972 long=122.431297")
        all_objs = storage.all().values()
        obj = max(all_objs, key=lambda x: x.created_at)
        self.assertEqual(obj.lat, 37.773972)
        self.assertEqual(obj.long, 122.431297)

    def test_create_with_strings(self):
        """Test create command with string parameters"""
        self.console.do_create("Place name=\"Ile_Ayo\" city_id=\"0001\"")
        all_objs = storage.all().values()
        obj = max(all_objs, key=lambda x: x.created_at)
        self.assertEqual(obj.name, "Ile Ayo")
        self.assertEqual(obj.city_id, "0001")

    def test_create_with_quoted_strings(self):
        """Test create command with quoted strings in a string parameter"""
        self.console.do_create("Place desc=\"A_place_to_\"Turaka\"!")
        all_objs = storage.all().values()
        obj = max(all_objs, key=lambda x: x.created_at)
        self.assertEqual(obj.desc, 'A place to "Turaka"!')


if __name__ == "__main__":
    unittest.main()
