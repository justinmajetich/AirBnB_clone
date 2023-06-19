#!/usr/bin/python3

import unittest
import sys
import io
from contextlib import contextmanager
from unittest.mock import patch
from io import StringIO
from models import *
from datetime import datetime
from console import HBNBCommand
from models.base_model import BaseModel


class Test_Console(unittest.TestCase):
    """
    Test the console
    """

    def setUp(self):
        self.cli = HBNBCommand()

        test_args = {'updated_at': datetime(2017, 2, 11, 23, 48, 34, 339879),
                     'id': 'd3da85f2-499c-43cb-b33d-3d7935bc808c',
                     'created_at': datetime(2017, 2, 11, 23, 48, 34, 339743),
                     'name': 'Ace'}
        self.model = BaseModel(test_args)
        self.model.save()

    """def tearDown(self):
        with patch('sys.stdout', new=StringIO()) as f:
            com = "destroy BaseModel d3da85f2-499c-43cb-b33d-3d7935bc808c"
            self.cli.onecmd(com)"""

    def test_show_error_no_args(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show ''")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show_error_missing_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_not_good_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show Human 1234-5678-9101")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel {}".format(output))
        self.assertFalse(output in f.getvalue())

    def test_create_with_args(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create State name=\"Alaska\"")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show State{}".format(output))
        self.assertFalse(output in f.getvalue())
