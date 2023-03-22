#!/usr/bin/python3
""" Modules for Console tests"""
import unittest
from models.base_model import BaseModel
from console import HBNBCommand


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
        self.assertIsInstance(sys.stdout.getvalue(), str)

    def test_create_error1(self):
        """ test the create command """
        console = self.create()
        console.onecmd("create")
        self.assertEqual(sys.stdout.getvalue(), "** class name missing **")
    
    def test_create_error2(self):
        """ test the create command """
        console = self.create()
        console.onecmd("create blabla")
        self.assertEqual(sys.stdout.getvalue(), "** class doesn't exist **")
    
    def test_show(self):
        """ test the show command """
        console = self.create()
        console.onecmd("create City")
        city_id = sys.stdout.getvalue()
        console.onecmd(f"show City {city.id}")
        self.assertIsInstance(sys.stdout.getvalue(), str)

    def test_show_error1(self):
        """ test the show command """
        console = self.create()
        console.onecmd("create City")
        city_id = sys.stdout.getvalue()
        console.onecmd(f"show")
        self.assertEqual(sys.stdout.getvalue(), "** class name missing **")

    def test_show_error2(self):
        """ test the show command """
        console = self.create()
        console.onecmd("create City")
        city_id = sys.stdout.getvalue()
        console.onecmd(f"show City")
        self.assertEqual(sys.stdout.getvalue(), "** instance id missing **")

    def test_show_error2(self):
        """ test the show command """
        console = self.create()
        console.onecmd("create City")
        city_id = sys.stdout.getvalue()
        console.onecmd(f"show Bla {city.id}")
        self.assertEqual(sys.stdout.getvalue(), "** class doesn't exist **")

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
        self.assertIn("Gabriel", sys.stdout.getvalue())

    def test_count(self):
        """ test the count command """
        console = self.create()
        console.onecmd("create City")
        self.assertEqual('2', HBNBCommand.count())
    
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
        self.assertEqual("instance id missing", sys.stdout.getvalue())
    