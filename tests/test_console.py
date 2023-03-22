#!/usr/bin/python3
""" Modules for Console tests"""
import unittest
from models.base_model import BaseModel
from console import HBNBCommand
import sys
from io import StringIO
import io


class TestConsole(unittest.TestCase):
    """ tests console """
    def create(self):
        """ creates an instance of interpreter """
        return HBNBCommand()
    
    def test_quit(self):
        """ test the quit command """
        console = self.create()
        self.assertTrue(console.onecmd("quit"))
    
    def test_EOF(self):
        """ test the EOF command """
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_create_normal(self):
        """ test the create command """
        console = self.create()
        console.onecmd("create City")
        out = StringIO()
        self.assertIsInstance(out.getvalue(), str)

    def test_create_error1(self):
        """ test the create command """
        console = self.create()
        console.onecmd("create")
        sys.stdout = io.StringIO()
        out = sys.stdout.getvalue()
        self.assertEqual(out, "** class name missing **")
    
    def test_create_error2(self):
        """ test the create command """
        console = self.create()
        console.onecmd("create blabla")
        sys.stdout = io.StringIO()
        out = sys.stdout.getvalue()
        self.assertEqual(out, "** class doesn't exist **")
    
    def test_show(self):
        """ test the show command """
        console = self.create()
        console.onecmd("create City")
        city_id = sys.stdout.getvalue()
        console.onecmd(f"show City {city.id}")
        self.assertIsInstance(StringIO().getvalue(), str)

    def test_show_error1(self):
        """ test the show command """
        console = self.create()
        console.onecmd("create City")
        console.onecmd(f"show")
        sys.stdout = io.StringIO()
        out = sys.stdout.getvalue()
        self.assertEqual(out, "** class name missing **")

    def test_show_error2(self):
        """ test the show command """
        console = self.create()
        console.onecmd("create City")
        console.onecmd(f"show City")
        sys.stdout = io.StringIO()
        out = sys.stdout.getvalue()
        self.assertEqual(out, "** instance id missing **")

    def test_show_error2(self):
        """ test the show command """
        console = self.create()
        console.onecmd("create City")
        city_id = StringIO().getvalue()
        output = console.onecmd(f"show Bla {city.id}")
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_error1(self):
        """ test the destroy command """
        console = self.create()
        console.onecmd("create City")
        console.onecmd(f"destroy City")
        self.assertEqual(sys.stdout.getvalue(), "** instance id missing **")

    def test_destroy_error2(self):
        """ test the destroy command """
        console = self.create()
        console.onecmd("create City")
        city_id = sys.stdout.getvalue()
        console.onecmd(f"destroy Bla {city_id}")
        self.assertEqual(sys.stdout.getvalue(), "** class doesn't exist **")

    def test_destroy_error3(self):
        """ test the destroy command """
        console = self.create()
        console.onecmd("create City")
        city_id = sys.stdout.getvalue()
        console.onecmd(f"destroy {city_id}")
        self.assertEqual(sys.stdout.getvalue(), "** class name missing **")

    def test_all(self):
        """ test the all command """
        console = self.create()
        console.onecmd("create User first_name = 'Gabriel' email='test@mail.com' password='g@br!el'")
        console.onecmd("all")
        sys.stdout = StringIO()
        out = sys.stdout.getvalue()
        self.assertIn("Gabriel", out)

    def test_count(self):
        """ test the count command """
        console = self.create()
        console.onecmd("create City")
        self.assertEqual('2', self.count())
    
    def test_update_1(self):
        """ test the update command """
        console = self.create()
        console.onecmd("create User")
        console.onecmd("update User")
        self.assertEqual("instance id missing", sys.stdout.getvalue())

    def test_update_2(self):
        """ test the update command """
        console = self.create()
        console.onecmd("create User")
        console.onecmd("update User")
        output = StringIO()
        out = output.getvalue()
        self.assertEqual("instance id missing", out)
    