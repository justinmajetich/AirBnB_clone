#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO 
from console import HBNBCommand
""" Module for console tests """


class test_console(unittest.TestCase):
    """ Tests for the console """
    
    def test_help(self):
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            c = f.getvalue()
            self.assertEqual(c, f.getvalue())

    def test_create(self):
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            c = f.getvalue()
            self.assertEqual(c, f.getvalue())

    def test_show(self):
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            c = f.getvalue()
            HBNBCommand().onecmd("update BaseModel {}".format(c))
            c = f.getvalue()
            self.assertEqual(c, f.getvalue())
