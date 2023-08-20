#!/usr/bin/python3
"""
Unit tests for the Console class
"""

import unittest
import os
import pycodestyle
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestConsoleClass(unittest.TestCase):
    """Tests the Console class"""

    def setUp(self):
        """Set up the test environment"""
        with open("test.json", "w"):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down the test environment"""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_pycodestyle(self):
        """Check console and test_console conform to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(["console.py", "tests/test_console.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_permissions(self):
        """Check if the file has the necessary permissions to be executed"""
        file = "console.py"
        self.assertTrue(os.access(file, os.F_OK))
        self.assertTrue(os.access(file, os.R_OK))
        self.assertTrue(os.access(file, os.W_OK))
        self.assertTrue(os.access(file, os.X_OK))

    def test_module_doc(self):
        """Check module documentation"""
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_class_doc(self):
        """Check class documentation"""
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_methods_doc(self):
        """Check methods documentation"""
        for method in dir(HBNBCommand):
            self.assertTrue(len(method.__doc__) > 0)

    def test_help_msgs(self):
        """Checks if all commands have a help message"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("help create")
            self.assertGreater(len(msg.getvalue()), 0)
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("help show")
            self.assertGreater(len(msg.getvalue()), 0)
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("help destroy")
            self.assertGreater(len(msg.getvalue()), 0)
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("help all")
            self.assertGreater(len(msg.getvalue()), 0)
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("help update")
            self.assertGreater(len(msg.getvalue()), 0)

    def test_create(self):
        """Tests if the create method works as intended"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create BaseModel")
            self.assertGreater(len(msg.getvalue()), 0)

    def test_create_empty(self):
        """Tests the create method with no parameters"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create")
            self.assertEqual(msg.getvalue(), "** class name missing **\n")

    def test_create_unknown(self):
        """Tests the create method with unknown class name"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create Unknown")
            self.assertEqual(msg.getvalue(), "** class doesn't exist **\n")

    def test_create_all(self):
        """Tests the create method with all"""
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('all State')
            self.assertGreater(len(msg.getvalue()), 0)

    def test_create_no_name(self):
        """Tests the create method without a name"""
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('create State name="California"')
            self.assertGreater(len(msg.getvalue()), 0)

    def test_create_non_existing(self):
        """Tests the show method with non existing class name"""
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('create State name="California"')
            self.assertGreater(len(msg.getvalue()), 0)
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('all State')
            self.assertIn("California", msg.getvalue())

    def test_create_underscore(self):
        """Tests the create method with an underscore"""
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('create State name="California_is_life"')
            self.assertGreater(len(msg.getvalue()), 0)
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('all State')
            self.assertIn("California is life", msg.getvalue())

    def test_create_int(self):
        """Tests the create method with an integer"""
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('create State money=500')
            self.assertGreater(len(msg.getvalue()), 0)
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('all State')
            self.assertIn("500", msg.getvalue())

    def test_create_int_error(self):
        """Tests the create method with an integer and a string"""
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('create State name=5055m')
            self.assertGreater(len(msg.getvalue()), 0)
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('all State')
            self.assertNotIn("5055m", msg.getvalue())

    def test_create_float(self):
        """Tests the create method with a float"""
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('create State people=2.5')
            self.assertGreater(len(msg.getvalue()), 0)
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('all State')
            self.assertIn("2.5", msg.getvalue())

    def test_create_float_error(self):
        """Tests the create method with a period '.' and a string"""
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('create State name=hello.world')
            self.assertGreater(len(msg.getvalue()), 0)
        with patch('sys.stdout', new=StringIO()) as msg:
            HBNBCommand().onecmd('all State')
            self.assertNotIn("hello.world", msg.getvalue())

    def test_show(self):
        """Tests if the show method works as intended"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create BaseModel")
            class_id = msg.getvalue()
            self.assertGreater(len(class_id), 0)
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd(f"show BaseModel {class_id}")
            self.assertNotEqual(msg.getvalue(), "** no instance found **\n")

    def test_show_alt(self):
        """Test an alternative way with
        the show method using [class_name].show"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create User")
            user_id = msg.getvalue()
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd(f'User.show("{user_id}")')
            self.assertGreater(len(msg.getvalue()), 0)

    def test_show_non_existing(self):
        """Tests the show method with non existing class name"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("show NonExisting")
            self.assertEqual(msg.getvalue(), "** class doesn't exist **\n")

    def test_show_empty(self):
        """Tests the show method with no parameters"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("show")
            self.assertEqual(msg.getvalue(), "** class name missing **\n")

    def test_show_id(self):
        """Tests the show method without a class id"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(msg.getvalue(), "** instance id missing **\n")

    def Test_destroy(self):
        """Tests if the destroy method works as intended"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create BaseModel")
            class_id = msg.getvalue()
            self.assertGreater(len(class_id), 0)
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd(f"destroy BaseModel {class_id}")
            self.assertNotEqual(msg.getvalue(), "** no instance found **\n")

    def test_destroy_empty(self):
        """Tests the destroy method with no parameters"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(msg.getvalue(), "** class name missing **\n")

    def test_destroy_non_existing(self):
        """Tests the destroy method with non existing class name"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("destroy NonExisting")
            self.assertEqual(msg.getvalue(), "** class doesn't exist **\n")

    def test_destroy_id(self):
        """Tests the destroy method without a class id"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(msg.getvalue(), "** instance id missing **\n")

    def test_destroy_equal(self):
        """Tests if the class is id associated with the class name"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("destroy BaseModel 69420")
            self.assertEqual(msg.getvalue(), "** no instance found **\n")

    def test_all(self):
        """Tests if the all method works as intended"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("all BaseModel")
            self.assertGreater(len(msg.getvalue()), 0)

    def test_all_alt(self):
        """Test an alternative way with
        the all method using [class_name].all"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create User")
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("User.all()")
            self.assertGreater(len(msg.getvalue()), 0)

    def test_all_all(self):
        """Tests if the all method works as intended"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("all")
            self.assertGreater(len(msg.getvalue()), 0)

    def test_all_non_existing(self):
        """Tests the all method with non existing class name"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("all NonExisting")
            self.assertEqual(msg.getvalue(), "** class doesn't exist **\n")

    def test_update_empty(self):
        """Tests the update method with no parameters"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("update")
            self.assertEqual(msg.getvalue(), "** class name missing **\n")

    def test_update_non_existing(self):
        """Tests the update method with non existing class name"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("update NonExisting")
            self.assertEqual(msg.getvalue(), "** class doesn't exist **\n")

    def test_update_id(self):
        """Tests the update method without a class id"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(msg.getvalue(), "** instance id missing **\n")

    def test_update_equal(self):
        """Tests if the class is id associated with the class name"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("update BaseModel 69420")
            self.assertEqual(msg.getvalue(), "** no instance found **\n")

    def test_update_no_name(self):
        """Tests the update method without a name"""
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd("create BaseModel")
            class_id = msg.getvalue()
            self.assertGreater(len(class_id), 0)
        with patch("sys.stdout", new=StringIO()) as msg:
            HBNBCommand().onecmd(f"update BaseModel {class_id}")
            self.assertEqual(msg.getvalue(), "** attribute name missing **\n")


if __name__ == "__main__":
    unittest.main()
