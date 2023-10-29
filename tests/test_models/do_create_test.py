#!/usr/bin/python3
"""
Unittests for create command in HBNB console
"""

import unittest
import io
import sys
from models.engine.file_storage import FileStorage
from console import HBNBCommand

import unittest
import io
from contextlib import redirect_stdout
from console import HBNBCommand

class TestConsoleCreate(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_create_missing_class_name(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.console.onecmd("create")
            output = buf.getvalue()
            self.assertEqual(output, "** class name missing **\n")

    def test_create_invalid_class_name(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.console.onecmd("create InvalidClass")
            output = buf.getvalue()
            self.assertEqual(output, "** class doesn't exist **\n")

    def test_create_missing_parameters(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.console.onecmd("create BaseModel")
            output = buf.getvalue()
            self.assertEqual(output, "f0d65a2d-66e3-4cf5-84f1-6910c2f23f83\n")

    def test_create_valid_instance(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.console.onecmd('create BaseModel name="My House" number=42')
            output = buf.getvalue()
            self.assertTrue(len(output) == 36)

    def test_create_invalid_integer_value(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.console.onecmd('create BaseModel count=invalid')
            output = buf.getvalue()
            self.assertEqual(output, "** invalid parameter format **\n")

    def test_create_invalid_float_value(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.console.onecmd('create BaseModel rate=invalid.2')
            output = buf.getvalue()
            self.assertEqual(output, "** invalid float value **\n")

    def test_create_invalid_string_format(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.console.onecmd('create BaseModel name=My_Invalid_House')
            output = buf.getvalue()
            self.assertEqual(output, "** invalid parameter format **\n")

if __name__ == "__main__":
    unittest.main()
