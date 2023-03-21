#!/usr/bin/env python3
"""
A unit test module for testing ``console.py`` module.
"""

from console import HBNBCommand
import unittest
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """
    Test the basic features of the Console.
    """

    def test_console_helper(self):
        """
        Testing the console helper method, being one of the
        default available command that come with cmd.Cmd.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
        self.assertIn("Documented commands", output)

    def test_console_quit(self):
        """
        Testing the console helper method, being one of the
        default available command that come with cmd.Cmd.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            output = f.getvalue()
        self.assertIn("", output)

    def test_console_EOF(self):
        """
        Testing the console helper method, being one of the
        default available command that come with cmd.Cmd.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            output = f.getvalue()
        self.assertIn("", output)

    def test_create_and_show_on_all_instances(self):
        """
        Testing create and show command against creating
        an instance of BaseModel, User, State, City,
        Amenity, Place, and Review.
        """
        all_class = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']
        for test_class in all_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(test_class))
                obj_id = f.getvalue()
                HBNBCommand().onecmd("show {} {}".format(test_class,
                                                         obj_id))
                output = f.getvalue()
            self.assertIn(obj_id, output)
            self.assertIn("created_at", output)

    def test_all_command_output(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        all_class = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']
        for test_class in all_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(test_class))
                obj_id = f.getvalue()
                HBNBCommand().onecmd("all")
                output = f.getvalue()
                self.assertIn(test_class, output)
                self.assertIn(obj_id, output)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(test_class))
                obj_id = f.getvalue()
                HBNBCommand().onecmd("all {}".format(test_class))
                output = f.getvalue()
                self.assertIn(test_class, output)
                self.assertIn(obj_id, output)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(test_class))
                obj_id = f.getvalue()
                HBNBCommand().onecmd("all MyModel")
                output = f.getvalue()
                self.assertIn("** class doesn't exist **", output)

    def test_userall_command_output(self):
        """
        This method of this test class tests for exactly
        what the user.all command reads.
        """
        all_class = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']
        for test_class in all_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.all()".format(test_class))
                output = f.getvalue()
            self.assertIn(test_class, output)
            self.assertIn("created_at", output)

    def test_classcount_command_output(self):
        """
        This method of this test class tests for exactly
        what the class.count command reads.
        """
        all_class = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']
        for test_class in all_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(test_class))
                HBNBCommand().onecmd("create {}".format(test_class))
                HBNBCommand().onecmd("{}.count()".format(test_class))
                output = f.getvalue()
            self.assertIn("2", output)

    def test_classshow_command_output(self):
        """
        This method of this test class tests for exactly
        what the class.show command reads.
        """
        all_class = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']
        for test_class in all_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(test_class))
                obj_id = f.getvalue()
                HBNBCommand().onecmd("{}.show({})".format(test_class, obj_id))
                output = f.getvalue()
            self.assertIn(obj_id, output)

    def test_destroy_command(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        all_class = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']
        for test_class in all_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(test_class))
                obj_id2 = f.getvalue()
                HBNBCommand().onecmd("create BaseModel")
                obj_id = f.getvalue()
                HBNBCommand().onecmd("destroy BaseModel {}".format(obj_id))
                HBNBCommand().onecmd("{}.destroy({})".format(test_class,
                                                             obj_id2))
                output2 = f.getvalue()
                HBNBCommand().onecmd("show {} {}".format(test_class, obj_id2))
                output = f.getvalue()
                HBNBCommand().onecmd("show BaseModel {}".format(obj_id))
                output = f.getvalue()
            self.assertIn("** no instance found **", output)
            self.assertIn("** no instance found **", output2)

    def test_improved_create_command(self):
        """
        This method tests for the imporved functionalities of create
        command with the console.
        """
        all_class = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']
        all_types = ['\"John_Doe\"', '89', '3.1416']

        for test_class in all_class:
            for test_type in all_types:
                with patch('sys.stdout', new=StringIO()) as f:
                    cmd = "create {} var={}".format(test_class, test_type)
                    HBNBCommand().onecmd(cmd)
                    test_id = f.getvalue()
                    cmd = "show {} {}".format(test_class, test_id)
                    HBNBCommand().onecmd(cmd)
                    output = f.getvalue()
                    self.assertIn('var', output)
                    self.assertIn(test_type.strip('"').replace('_', ' '),
                                  output)

    def test_update_command(self):
        """
            This method in this tests for the update command
        """
        all_class = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']
        for test_class in all_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(test_class))
                obj_id = f.getvalue()
                cmd = "update {} {} name hbnb".format(test_class, obj_id)
                HBNBCommand().onecmd(cmd)
                cmd3 = "{}.update({}, first_name, alxhbnb\
                                  )".format(test_class, obj_id)
                HBNBCommand().onecmd(cmd3)
                cmd4 = "{}.update({}, last_name, alxholberton\
                                  )".format(test_class, obj_id)
                HBNBCommand().onecmd(cmd4)
                HBNBCommand().onecmd("show {} {}".format(test_class, obj_id))
                output = f.getvalue()
            self.assertIn("'name': 'hbnb'", output)
            self.assertIn("'first_name': 'alxhbnb'", output)
