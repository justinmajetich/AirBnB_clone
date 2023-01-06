#!/usr/bin/python3
""" Defines tests for the console module: HBNBCommand class. Therefore tests
the commands: quit, EOF, all, show, create, update and destroy """
import os
import sys
from io import StringIO
import unittest
from unittest.mock import patch
from models import storage
from console import HBNBCommand


class Test_prompting(unittest.TestCase):
    """ Test prompting of the console """

    def test_prompt_string(self):
        """ test that the prompt is '(hbnb) '"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """ test that cmd's emptyline method is overriden: returns nothing """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("")
            self.assertEqual("", output.getvalue().strip())


class Test_help(unittest.TestCase):
    """ Test help messaging of the console """

    def test_help_quit(self):
        """ test that 'help quit' cmd returns a help message """
        messg = "Exits the program with formatting"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(messg, output.getvalue().strip())

    def test_help_EOF(self):
        """ test that 'help EOF' cmd returns a help message """
        messg = "Exits the program without formatting"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(messg, output.getvalue().strip())

    def test_help_create(self):
        """ test that 'help create' cmd returns a help message """
        messg = "Creates a class of any type\n[Usage]: create <className>"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help create")
            self.assertEqual(messg, output.getvalue().strip())


class Test_Exit(unittest.TestCase):
    """ Define tests for the exit cmds (EOF and quit) """

    def test_quit(self):
        """ test that 'quit' exits the console/interpreter """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """ test that 'EOF/ Ctrl + D' exits the console/interpreter """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class Test_Create(unittest.TestCase):
    """ Define tests for the create cmd """
    # setup the test environment

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    # detroy(tear down) the test environment
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    # ++++++ Actual Create_Tests +++++ #
    def test_create_without_class(self):
        """ test that  cmd <create> fails if class is undefined """
        res = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create')
            self.assertEqual(output.getvalue().strip(), res)

    def test_create_with_invalid_class(self):
        """ test that  cmd <create> <cls> fails if argument is an
            undefined class
        """
        res = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create MyModel')
            self.assertEqual(output.getvalue().strip(), res)

    def test_create_with_valid_class(self):
        """ test that  cmd <create> <cls> instantiates a defined class """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create BaseModel')
            res_id = output.getvalue().strip()
            objs = storage.all()
            new_key = 'BaseModel.{}'.format(res_id)
            self.assertTrue(new_key in objs.keys())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create User')
            res_id = output.getvalue().strip()
            objs = storage.all()
            new_key = 'User.{}'.format(res_id)
            self.assertTrue(new_key in objs.keys())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create State')
            res_id = output.getvalue().strip()
            objs = storage.all()
            new_key = 'State.{}'.format(res_id)
            self.assertTrue(new_key in objs.keys())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create City')
            res_id = output.getvalue().strip()
            objs = storage.all()
            new_key = 'City.{}'.format(res_id)
            self.assertTrue(new_key in objs.keys())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create Place')
            res_id = output.getvalue().strip()
            objs = storage.all()
            new_key = 'Place.{}'.format(res_id)
            self.assertTrue(new_key in objs.keys())

    def test_create_with_valid_parameters(self):
        """ test that cmd <create> <cls> <parameter> instantiates a defined
        class with attributes created from the parameters.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create User name="John_Doe" age=26')
            res_id = output.getvalue().strip()
            objs = storage.all()
            new_key = 'User.{}'.format(res_id)
            self.assertTrue(new_key in objs.keys())
            self.assertTrue('name' and 'age' in objs[new_key].__dict__.keys())

    def test_create_skips_invalid_parameters(self):
        """ test that  cmd <create> <cls> <invalid/unrecognizable parameter(s)>
        skips the parameters. i.e. it does not create attributes from them
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create City\
                    name="Los Angeles" state="California"')
            res_id = output.getvalue().strip()
            objs = storage.all()
            new_key = 'City.{}'.format(res_id)
            self.assertTrue(new_key in objs.keys())
            self.assertTrue('state' in objs[new_key].__dict__.keys())
            self.assertFalse('name' in objs[new_key].__dict__.keys())

    def test_create_subsititutes_underscores_in_parameter_values(self):
        """ test that  cmd <create> <cls> <valid parameter(s)> substitutes
        underscores in parameter values with spaces
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create City\
                    name="Los_Angeles" state="California"')
            res_id = output.getvalue().strip()
            objs = storage.all()
            new_key = 'City.{}'.format(res_id)
            self.assertTrue(new_key in objs.keys())
            self.assertTrue(
                'state' and 'name' in objs[new_key].__dict__.keys())
            self.assertFalse('Los_Angeles' in objs[new_key].__dict__.values())


class Test_Show(unittest.TestCase):
    """ Define tests for the show cmd """
    pass


class Test_Update(unittest.TestCase):
    """ Define tests for the update cmd """
    pass


class Test_Destroy(unittest.TestCase):
    """ Define tests for the destroy cmd """
    pass


class Test_Count(unittest.TestCase):
    """ Define tests for the count cmd """
    pass


class Test_All(unittest.TestCase):
    """ Define tests for the all cmd """
    pass
