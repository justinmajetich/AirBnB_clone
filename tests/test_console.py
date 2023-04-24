#!/usr/bin/env python3
"""Module for TestHBNBCommand class."""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
import sys
import re
import os


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Sets up test cases."""
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def test_help(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands", f.getvalue().strip())

    def test_help_EOF(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        self.assertIn("EOF command to exit the program", f.getvalue())

    def test_help_all(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        self.assertIn("Prints all string representation", f.getvalue())

    def test_help_count(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
        self.assertIn("Retrieve the number of instances", f.getvalue())

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIn("Quit command to exit", f.getvalue().strip())

    def test_help_update(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        self.assertIn("Updates an instance based", f.getvalue())

    def test_do_create(self):
        """Tests create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertIn(f.getvalue().strip(), "** class name missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create new")
            self.assertIn(f.getvalue().strip(), "** class doesn't exist **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertRegex(f.getvalue(), r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
    def test_create_valid_attributes(self):
        "Test with valid elements"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User name='John' age=25")
            output = f.getvalue().strip()
            self.assertRegex(output, r"\b\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\b")
            self.assertTrue(User.get(output))

    def test_create_invalid_attribute_name(self):
        "Test creating an object with invalid attribute name:"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User invalid_name='John'")
            output = f.getvalue().strip()
            self.assertEqual(output, "** invalid attribute name **")

    def test_create_invalid_attribute_value(self):
        "Test creating an object with invalid attribute value:"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User name=123")
            output = f.getvalue().strip()
            self.assertEqual(output, "** invalid attribute value **")

    def test_create_missing_class_name(self):
        "Test creating an object with missing class name:"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_non_existent_class_name(self):
        "Test creating an object with non-existent class name:"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create NonExistentClass")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show(self):
        """Tests show for all classes"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(obj_id))
            self.assertIn(obj_id, f.getvalue().strip())

    def test_show_error(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertIn("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertIn("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234")
            self.assertIn("** no instance found **", f.getvalue().strip())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel {}".format(obj_id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(obj_id))
            self.assertIn("** no instance found **", f.getvalue().strip())

    def test_destroy_error(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertIn("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertIn("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234")
            self.assertIn("** no instance found **", f.getvalue().strip())

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {obj_id} name 'test'")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(obj_id))
            self.assertIn("'name': 'test'", f.getvalue().strip())

    def test_update_error(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertIn("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertIn("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234")
            self.assertIn("** no instance found **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {}".format("1234"))
            self.assertIn("** no instance found **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {} name".format("1234"))
            self.assertIn("** no instance found **", f.getvalue().strip())

    def test_all_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn("[BaseModel]", f.getvalue().strip())

    def test_destroy_valid(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel {}".format(obj_id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(obj_id))
            self.assertIn("** no instance found **", f.getvalue().strip())

    def test_destroy_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel 1234")
            self.assertIn("** class doesn't exist **", f.getvalue().strip())

    def test_destroy_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234")
            self.assertIn("** no instance found **", f.getvalue().strip())

    def test_update_valid(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {obj_id} name 'test'")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(obj_id))
            self.assertIn("'name': 'test'", f.getvalue().strip())

    def test_update_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel 1234 name 'test'")
            self.assertIn("** class doesn't exist **", f.getvalue().strip())

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertIn('Prints the string representation', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        self.assertIn('Creates a new instance of the class', f.getvalue())

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertIsInstance(f.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1111")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1111")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertIsInstance(f.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        self.assertIsInstance(f.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1111")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        model_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {model_id}")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {model_id} first")
        self.assertEqual(f.getvalue(), '** value missing **\n')

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        self.assertEqual(f.getvalue(), '')

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(f.getvalue(), '\n')

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
        self.assertEqual(f.getvalue(), '')

    def test_basedotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
        self.assertNotIn('[City]', f.getvalue())
        self.assertNotIn('[Review]', f.getvalue())
        self.assertNotIn('[Place]', f.getvalue())
        self.assertNotIn('[Amenity]', f.getvalue())
        self.assertNotIn('[State]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all")
        self.assertIn('**', f.getvalue())

    def test_reviewdotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
        self.assertNotIn('[BaseModel]', f.getvalue())
        self.assertNotIn('[User]', f.getvalue())
        self.assertNotIn('[State]', f.getvalue())
        self.assertNotIn('[Place]', f.getvalue())
        self.assertNotIn('[City]', f.getvalue())
        self.assertNotIn('[Amenity]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all")
        self.assertIn('**', f.getvalue())

    def test_userdotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        self.assertNotIn('[BaseModel]', f.getvalue())
        self.assertNotIn('[City]', f.getvalue())
        self.assertNotIn('[Review]', f.getvalue())
        self.assertNotIn('[Place]', f.getvalue())
        self.assertNotIn('[Amenity]', f.getvalue())
        self.assertNotIn('[State]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all")
        self.assertIn('**', f.getvalue())

    def test_statedotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
        self.assertNotIn('[BaseModel]', f.getvalue())
        self.assertNotIn('[City]', f.getvalue())
        self.assertNotIn('[Review]', f.getvalue())
        self.assertNotIn('[Place]', f.getvalue())
        self.assertNotIn('[Amenity]', f.getvalue())
        self.assertNotIn('[User]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all")
        self.assertIn('***', f.getvalue())

    def test_placedotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
        self.assertNotIn('[BaseModel]', f.getvalue())
        self.assertNotIn('[City]', f.getvalue())
        self.assertNotIn('[Review]', f.getvalue())
        self.assertNotIn('[State]', f.getvalue())
        self.assertNotIn('[Amenity]', f.getvalue())
        self.assertNotIn('[User]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all")
        self.assertIn('**', f.getvalue())

    def test_amenitydotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
        self.assertNotIn('[BaseModel]', f.getvalue())
        self.assertNotIn('[City]', f.getvalue())
        self.assertNotIn('[Review]', f.getvalue())
        self.assertNotIn('[Place]', f.getvalue())
        self.assertNotIn('[State]', f.getvalue())
        self.assertNotIn('[User]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all")
        self.assertIn('**', f.getvalue())

    def test_citydotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
        self.assertNotIn('[BaseModel]', f.getvalue())
        self.assertNotIn('[State]', f.getvalue())
        self.assertNotIn('[Review]', f.getvalue())
        self.assertNotIn('[Place]', f.getvalue())
        self.assertNotIn('[Amenity]', f.getvalue())
        self.assertNotIn('[User]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all")
        self.assertIn('**', f.getvalue())

    def test_basedotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_userdotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_statedotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_placedotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_citydotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_amenitydotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_reviewdotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_basedotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show(\"{model_id}\")")
        self.assertIn('[BaseModel]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_userdotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
            self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show(\"{obj_id}\")")
            self.assertIn('[User]', f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show(idf)")
            self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_citydotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show(\"{model_id}\")")
        self.assertIn('[City]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_statedotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show(\"{model_id}\")")
        self.assertIn('[State]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_placedotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show(\"{model_id}\")")
        self.assertIn('[Place]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_amenitydotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show(\"{model_id}\")")
        self.assertIn('[Amenity]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_reviewdotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show(\"{model_id}\")")
        self.assertIn('[Review]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_reviewdotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy(\"{model_id}\")")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_basedotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy(\"{model_id}\")")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_userdotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy(\"{model_id}\")")
            self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_placedotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy(\"{model_id}\")")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_statedotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.destroy(\"{model_id}\")")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_citydotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy(\"{model_id}\")")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_amenitydotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy(\"{model_id}\")")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_basedotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update(\"{model_id}\")")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update(\"{model_id}\", first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update(\"{model_id}\", first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show(\"{model_id}\")")
        self.assertIn('first', f.getvalue())
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update(\"{model_id}\",
            {'second': 5, 'third': three})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show(\"{model_id}\")")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())
        """

    def test_userdotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update(\"{model_id}\")")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update(\"{model_id}\", first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update(\"{model_id}\", first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show(\"{model_id}\")")
        self.assertIn('first', f.getvalue())
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update(\"{model_id}\",
            {'second': 5, 'third': three})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show(\"{model_id}\")")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())
        """

    def test_placedotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update(\"{model_id}\")")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update(\"{model_id}\", first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update(\"{model_id}\", first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show(\"{model_id}\")")
        self.assertIn('first', f.getvalue())
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update(\"{model_id}\",
            {'second': 5, 'third': three})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show(\"{model_id}\")")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())
        """

    def test_statedotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update(\"{model_id}\")")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update(\"{model_id}\", first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update(\"{model_id}\", first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show(\"{model_id}\")")
        self.assertIn('first', f.getvalue())
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update(\"{model_id}\",
            {'second': 5, 'third': three})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show(\"{model_id}\")")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())
        """

    def test_citydotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update(\"{model_id}\")")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update(\"{model_id}\", first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update(\"{model_id}\", first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show(\"{model_id}\")")
        self.assertIn('first', f.getvalue())
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update(\"{model_id}\",
            {'second': 5, 'third': three})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show(\"{model_id}\")")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())
        """

    def test_amenitydotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update({model_id})")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update({model_id}, first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update(\"{model_id}\", first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show(\"{model_id}\")")
        self.assertIn('first', f.getvalue())
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update(\"{model_id}\",
            {'second': 5, 'third': three})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show(\"{model_id}\")")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())
        """

    def test_reviewdotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update(\"{model_id}\")")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update(\"{model_id}\", first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update(\"{model_id}\", first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show(\"{model_id}\")")
        self.assertIn('first', f.getvalue())
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update(\"{model_id}\",
            {'second': 5, 'third': three})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show(\"{model_id}\")")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())
        """
