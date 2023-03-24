#!/usr/bin/python3
"""Test file for the console"""
import unittest
from unittest.mock import patch
import io
import sys
from models.base_model import BaseModel
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_do_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.assertTrue(len(obj_id) > 0)
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create BaseModel name='test'")
            obj_id2 = f.getvalue().strip()
            self.assertTrue(len(obj_id2) > 0)
            self.assertNotEqual(obj_id, obj_id2)
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create BaseModel name='test' number=1")
            obj_id3 = f.getvalue().strip()
            self.assertTrue(len(obj_id3) > 0)
            self.assertNotEqual(obj_id, obj_id3)
            self.assertNotEqual(obj_id2, obj_id3)
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create BaseModel name='test' number=1.1")
            obj_id4 = f.getvalue().strip()
            self.assertTrue(len(obj_id4) > 0)
            self.assertNotEqual(obj_id, obj_id4)
            self.assertNotEqual(obj_id2, obj_id4)
            self.assertNotEqual(obj_id3, obj_id4)
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create BaseModel name='test' number=1.1 float=1.1")
            obj_id5 = f.getvalue().strip()
            self.assertTrue(len(obj_id5) > 0)
            self.assertNotEqual(obj_id, obj_id5)
            self.assertNotEqual(obj_id2, obj_id5)
            self.assertNotEqual(obj_id3, obj_id5)
            self.assertNotEqual(obj_id4, obj_id5)
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create BaseModel name='test' number=1.1 float=1.1 str='test'")
            obj_id6 = f.getvalue().strip()
            self.assertTrue(len(obj_id6) > 0)
            self.assertNotEqual(obj_id, obj_id6)
            self.assertNotEqual(obj_id2, obj_id6)
            self.assertNotEqual(obj_id3, obj_id6)
            self.assertNotEqual(obj_id4, obj_id6)
            self.assertNotEqual(obj_id5, obj_id6)
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create BaseModel name='test' number=1.1 float=1.1 str='test' list=[1, 2, 3]")
            obj_id7 = f.getvalue().strip()
            self.assertTrue(len(obj_id7) > 0)
            self.assertNotEqual(obj_id, obj_id7)
            self.assertNotEqual(obj_id2, obj_id7)
            self.assertNotEqual(obj_id3, obj_id7)
            self.assertNotEqual(obj_id4, obj_id7)
            self.assertNotEqual(obj_id5, obj_id7)
            self.assertNotEqual(obj_id6, obj_id7)

    def test_do_show(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("show MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("show BaseModel 1234")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("show BaseModel 1234 name='John'")
            self.assertEqual("** no instance found **\n", f.getvalue())


if __name__ == '__main__':
    unittest.main()
