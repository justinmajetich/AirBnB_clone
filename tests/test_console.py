#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class test_console(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.console.onecmd('destroy BaseModel')
            output = captured_output.getvalue().strip()
            self.assertTrue("** instance id missing **" in output)

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.console.onecmd('all')
            output = captured_output.getvalue().strip()
            self.assertTrue(output != "")

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.console.onecmd('count BaseModel')
            output = captured_output.getvalue().strip()
            self.assertTrue(output != "")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.console.onecmd('update BaseModel')
            output = captured_output.getvalue().strip()
            self.assertTrue("** instance id missing **" in output).getvalue().strip()
            self.assertTrue(output != "")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.console.onecmd('destroy BaseModel')
            output = captured_output.getvalue().strip()
            self.assertTrue("** instance id missing **" in output)

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.console.onecmd('all')
            output = captured_output.getvalue().strip()
            self.assertTrue(output != "")

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.console.onecmd('count BaseModel')
            output = captured_output.getvalue().strip()
            self.assertTrue(output != "")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.console.onecmd('update BaseModel')
            output = captured_output.getvalue().strip()
            self.assertTrue("** instance id missing **" in output)

    if __name__ == '__main__':
        unittest.main()