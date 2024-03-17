#!/usr/bin/python3

"""This module tests the console."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from lazy_methods import LazyMethods
import models

instance = LazyMethods()


class TestConsole(unittest.TestCase):
    """Tests the console."""

    def setUp(self):
        self.cli = HBNBCommand()

    def test_do_create_no_args(self):
        """Test `create` with no model name."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.cli.onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_invalid_class(self):
        """Test `create` with an invalid model name."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.cli.onecmd("create MyClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_create_valid_class(self):
        """Test `create` with a valid model name."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")
            self.assertNotEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_one_attribute(self):
        """Test `create` with one attribute."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.cli.onecmd('create BaseModel name="Holberton"')

            key = instance.get_key("BaseModel", instance.get_uuid(f))
            obj = models.storage.all()[key]
            self.assertDictContainsSubset({"name": "Holberton"}, obj.__dict__)

    def test_do_create_escaped_str(self):
        """Test `create` with an escaped string attribute value."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.cli.onecmd('create User first_name=""Betty"_Holberton"')

            key = instance.get_key("User", instance.get_uuid(f))
            obj = models.storage.all()[key]
            self.assertDictContainsSubset(
                {"first_name": '"Betty" Holberton'}, obj.__dict__
            )

    def test_do_create_multiple_attributes(self):
        """Test `create` with multiple attributes."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.cli.onecmd(
                'create User first_name="Betty" last_name="Holberton" '
                "age=98 salary=1000000.00"
            )

            key = instance.get_key("User", instance.get_uuid(f))
            obj = models.storage.all()[key]
            self.assertDictContainsSubset(
                {
                    "first_name": "Betty",
                    "last_name": "Holberton",
                    "age": 98,
                    "salary": 1000000.00,
                },
                obj.__dict__,
            )

    def test_do_create_invalid_attribute(self):
        """Test `create` with an invalid attribute."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.cli.onecmd('create User invalid_attribute="Betty Holberton"')

            key = instance.get_key("User", instance.get_uuid(f))
            obj = models.storage.all()[key]
            self.assertNotIn("invalid_attribute", obj.__dict__)


if __name__ == "__main__":
    unittest.main()
