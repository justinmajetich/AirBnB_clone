#!/usr/bin/python3
"""TestConsole Module"""
import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Tests the console"""

    def setUp(self):
        """SetUp"""
        pass

    def tearDown(self):
        """TearDown"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_create_method_without_args(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

    def test_create_method_with_wrong_class_name(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create wrong_class_name")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def test_create_method_work_as_fine(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        msg = f.getvalue()[:-1]
        self.assertRegex(msg, '\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')

    def test_create_method_accept_a_number_as_string(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place user_id=\"001\"")
            HBNBCommand().onecmd("all Place")
        msg = f.getvalue()[:-1]
        self.assertRegex(msg, "'user_id': '001'")

    def test_create_method_accept_attribute_value_with_underscore(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place name=\"My_little_house\"")
            HBNBCommand().onecmd("all Place")
        msg = f.getvalue()[:-1]
        self.assertRegex(msg, "'name': 'My little house'")

    def test_create_method_accept_attribute_value_with_positive_float(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place latitude=37.7739724")
            HBNBCommand().onecmd("all Place")
        msg = f.getvalue()[:-1]
        self.assertRegex(msg, "'latitude': 37.7739724")

    def test_create_method_accept_attribute_value_with_negative_float(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place longitude=-122.431297")
            HBNBCommand().onecmd("all Place")
        msg = f.getvalue()[:-1]
        self.assertRegex(msg, "'longitude': -122.431297")

    def test_create_method_accept_attribute_value_with_int(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place number_rooms=4")
            HBNBCommand().onecmd("all Place")
        msg = f.getvalue()[:-1]
        self.assertRegex(msg, "'number_rooms': 4")
