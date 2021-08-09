#!/usr/bin/python3
"""
    Contains the tests for class HBNBCommand
"""
import sys
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


def setUpModule():
    """Set up resources to be used in the test module"""
    if os.path.isfile("my_file.json"):
        os.rename("my_file.json", "tmp.json")


def tearDownModule():
    """Tear down resources used in the test module"""
    if os.path.isfile("my_file.json"):
        os.remove("my_file.json")
    if os.path.isfile("tmp.json"):
        os.rename("tmp.json", "my_file.json")


class TestHBNBCommand(unittest.TestCase):
    """Tests for the HBNBCommand prompt"""

    def test_HBNBCommand_prompt(self):
        """Test the HBNBCommand prompt"""
        self.assertEqual(HBNBCommand.prompt, '(hbnb) ')

    def test_empty_line(self):
        """Test output when an empty line is passed"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())


class TestHBNBCommand_create(unittest.TestCase):
    """Test the HBNBCommand create command"""

    def test_HBNBCommand_create_error_messages(self):
        """Test that the create comand prints the correct error messages"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('create'))
            self.assertEqual("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('create MyModel'))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_HBNBCommand_create_new_instances(self):
        """Test the creation of new instances of different classes"""

        Mm = ['BaseModel', 'User', 'Place',
              'City', 'State', 'Review', 'Amenity']
        for m in Mm:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create {}'.format(m)))
                new_key = m + "." + f.getvalue().strip()
                self.assertIn(new_key, storage.all().keys())


class TestHBNBCommand_show(unittest.TestCase):
    """Test the HBNBCommand show command"""

    def test_HBNBCommand_show_error_messages(self):
        """Test that the show comand prints the correct error messages"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('show'))
            self.assertEqual("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('show MyModel'))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('show BaseModel'))
            self.assertEqual("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('show BaseModel 12234321'))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_HBNBCommand_show_existing_instance(self):
        """Test the creation of new instances of different classes"""
        objs = storage.all()
        for key, value in objs.items():
            inst = key.split(".")
            value_str = str(value)
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().
                                 onecmd('show {} {}'.format(inst[0], inst[1])))
                self.assertEqual(value_str, f.getvalue().strip())


class TestHBNBCommand_dot_show(unittest.TestCase):
    """ Test the .show() command"""

    def test_HBNBCommand_dot_show_error_messages(self):
        """
            Test that the .show() comand prints the correct error messages
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('MyModel.show("")'))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('BaseModel.show("")'))
            self.assertEqual("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().
                             onecmd('BaseModel.show("12234321")'))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_HBNBCommand_dot_show_existing_instance(self):
        """
            Test the .show() command for an existing instance
        """
        Mm = ['BaseModel', 'User', 'Place',
              'City', 'State', 'Review', 'Amenity']
        my_objs = {}
        for m in Mm:
            tmp = eval(m)()
            tmp.save()
            tmp_id = m + "." + tmp.id
            my_objs[tmp_id] = tmp
        for key, val in my_objs.items():
            kk = key.split(".")
            value_str = str(val)
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('{}.\
                                 show("{}")'.format(kk[0], kk[1])))
                self.assertEqual(value_str, f.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """Test the HBNBCommand destroy command"""
    def test_HBNBCommand_destroy_error_messages(self):
        """Test that the destroy comand prints the correct error messages"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('destroy'))
            self.assertEqual("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('destroy MyModel'))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('destroy BaseModel'))
            self.assertEqual("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().
                             onecmd('destroy BaseModel 12234321'))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_HBNBCommand_destroy_existing_instances(self):
        """Test the destruction of new instances of different classes"""

        Mm = ['BaseModel', 'User', 'Place',
              'City', 'State', 'Review', 'Amenity']
        my_objs = {}
        for m in Mm:
            tmp = eval(m)()
            tmp.save()
            tmp_id = m + "." + tmp.id
            my_objs[tmp_id] = tmp
        for key in my_objs.keys():
            kk = key.split(".")
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().
                                 onecmd('destroy {} {}'.format(kk[0], kk[1])))
                objs = storage.all()
                self.assertNotIn(kk[1], objs.keys())


class TestHBNBCommand_dot_destroy(unittest.TestCase):
    """Test the HBNBCommand .destroy(<id>) command"""

    def test_HBNBCommand_dot_destroy_error_messages(self):
        """
            Test that the .destroy() comand prints the correct error messages
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('Mymodel.destroy("w")'))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('BaseModel.destroy("")'))
            self.assertEqual("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().
                             onecmd('BaseModel.destroy("12234321")'))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_HBNBCommand_dot_destroy_existing_instances(self):
        """
            Test the destruction of existing instances of different
            classes using .destroy(<id>)
        """
        Mm = ['BaseModel', 'User', 'Place',
              'City', 'State', 'Review', 'Amenity']
        my_objs = {}
        for m in Mm:
            tmp = eval(m)()
            tmp.save()
            tmp_id = m + "." + tmp.id
            my_objs[tmp_id] = tmp
        for key in my_objs.keys():
            kk = key.split(".")
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('{}\
                                 .destroy("{}")'.format(kk[0], kk[1])))
                objs = storage.all()
                self.assertNotIn(kk[1], objs.keys())


class TestHBNBCommand_all(unittest.TestCase):
    """Test the HBNBCommand all command"""

    def test_HBNBCommand_all_error_messages(self):
        """Test that the all comand prints the correct error messages"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('all MyModel'))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_HBNBCommand_all_existing_instances(self):
        """Test the creation of new instances of different classes"""

        objs = storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('all'))
            for key, value in objs.items():
                inst_key = key.split(".")[1]
                self.assertIn(inst_key, f.getvalue().strip())

    def test_HBNBCommand_all_existing_instances_specific_class(self):
        """Test the creation of new instances of different classes"""

        Mm = ['BaseModel', 'User', 'Place',
              'City', 'State', 'Review', 'Amenity']
        for m in Mm:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('all {}'.format(m)))
                for n in Mm:
                    if n != m:
                        self.assertNotIn(n, f.getvalue().strip())


class TestHBNBCommand_dot_all(unittest.TestCase):
    """
        Test the HBNBCommand .all()
    """
    def test_HBNBCommand_dot_all_error_messages(self):
        """
            Test is .all() command prints the correct error messages
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('MyModel.all()'))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_HBNBCommand_dot_all_existing_instances(self):
        """
            Test the .all() command with existing instances
        """
        Mm = ['BaseModel', 'User', 'Place',
              'City', 'State', 'Review', 'Amenity']
        for m in Mm:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('{}.all()'.format(m)))
                for n in Mm:
                    if n != m:
                        self.assertNotIn(n, f.getvalue().strip())


class TestHBNBCommand_update(unittest.TestCase):
    """Test the HBNBCommand update command"""

    def test_HBNBCommand_update_error_messages(self):
        """Test that the update comand prints the correct error messages"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('update'))
            self.assertEqual("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('update MyModel'))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('update BaseModel'))
            self.assertEqual("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('update BaseModel 12234321'))
            self.assertEqual("** no instance found **", f.getvalue().strip())

        objs = storage.all()
        for key, value in objs.items():
            kk = key.split(".")
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('update {} {}'.
                                                      format(kk[0], kk[1])))
                self.assertEqual("** attribute name missing **",
                                 f.getvalue().strip())

            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('update {} {} id'.
                                                      format(kk[0], kk[1])))
                self.assertEqual("** value missing **",
                                 f.getvalue().strip())

    def test_HBNBCommand_update_existing_instance(self):
        """Test the creation of new instances of different classes"""
        objs = storage.all()
        key = list(objs.keys())[0].split(".")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('update {} {} name Silvia'.
                                                  format(key[0], key[1])))
            self.assertFalse(HBNBCommand().onecmd('show {} {}'.
                                                  format(key[0], key[1])))
            self.assertIn('name', f.getvalue().strip())
            self.assertIn('Silvia', f.getvalue().strip())


class TestHBNBCommand_dot_update(unittest.TestCase):
    """
        Test .update() command
    """
    def test_HBNBCommand_dot_update_error_messages(self):
        """
            Test .update() prints the correct error messages
        """
        Mm = ['BaseModel', 'User', 'Place',
              'City', 'State', 'Review', 'Amenity']
        my_objs = {}
        for m in Mm:
            tmp = eval(m)()
            tmp.save()
            tmp_id = m + "." + tmp.id
            my_objs[tmp_id] = tmp
        for key in my_objs.keys():
            kk = key.split(".")
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('{}\
                                 .update(" ", " ", " ")'.format("MyModel")))
                self.assertEqual("** class doesn't exist **",
                                 f.getvalue().strip())

            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('{}\
                                 .update(" "," "," ")'.format(kk[0])))
                self.assertEqual("** no instance found **",
                                 f.getvalue().strip())

    def test_HBNBCommand_dot_update_existing_instance(self):
        """
            Test .update() command with existing instance
        """
        objs = storage.all()
        key = list(objs.keys())[0].split(".")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('{}.update("{}",\
                                                  "name", "Silvia")'.
                                                  format(key[0], key[1])))
            self.assertFalse(HBNBCommand().onecmd('show {} {}'.
                                                  format(key[0], key[1])))
            self.assertIn('name', f.getvalue().strip())
            self.assertIn('Silvia', f.getvalue().strip())


class TestHBNBCommand_dot_count(unittest.TestCase):
    """
        Test the HBNBCommand .count()
    """
    @classmethod
    def setUp(self):
        try:
            os.rename("my_file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("my_file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "my_file.json")
        except IOError:
            pass

    def test_HBNBCommand_dot_count_existing_instances(self):
        """
            Test the .count() command with existing instances
        """
        try:
            os.remove("my_file.json")
        except IOError:
            pass
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("2", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("2", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("2", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("2", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("2", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("2", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("2", f.getvalue().strip())


class TestHelpFunctionality(unittest.TestCase):
    """Test the help command functionality"""

    def test_help_no_argument(self):
        """Test output when help command used without argument"""
        msg = ("Documented commands (type help <topic>):\n"
               "========================================\n"
               "EOF  all  count  create  destroy  help  quit  show  update")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(msg, f.getvalue().strip())

    def test_help_EOF(self):
        """ test the help with with EOF """

        msg = ("Exit the command line")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(msg, f.getvalue().strip())

    def test_help_all(self):
        """ test the help with with all """

        msg = ("Prints all string representation of all instances.\
\nUsage: all or all <ClassName>")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(msg, f.getvalue().strip())

    def test_help_create(self):
        """ test the help with create """

        msg = ("Creates a new instance of BaseModel and saves \
it.\nUsage: create <ClassName>")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(msg, f.getvalue().strip())
    def test_help_destroy(self):
        """
            test the help with create
        """
        msg = "Deletes an instance based on the class name and id.\
\nUsage: destroy <ClassName> <id>"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(msg, f.getvalue().strip())

    def test_help_quit(self):
        """ test the help with quit """

        msg = ("Exit the command line.\nUsage: quit")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(msg, f.getvalue().strip())

    def test_help_show(self):
        """ test the help with show """

        msg = ("Prints the string representation of an instance \
based on the class name and id.\nUsage: show <ClassName> <id>.")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(msg, f.getvalue().strip())

    def test_help_update(self):
        """ test the help with update """

        msg = ("Updates an instance based on the class name and id\
by adding or changing attribute values.\
\nUsage: update <class name> <id> <attribute name> \"<attribute value>\"")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(msg, f.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
