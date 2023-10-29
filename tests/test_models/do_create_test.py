#!/usr/bin/python3
"""
Unittests for create command in HBNB console
"""

import unittest
import io
import sys
from models.engine.file_storage import FileStorage
from console import HBNBCommand

class TestConsoleWithFileStorage(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.fs = FileStorage()

    def tearDown(self):
        del self.console
        del self.fs

    def test_create_base_model(self):
        # Redirect stdout to capture console output
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()

        # Run the "create" command to create a BaseModel instance
        self.console.onecmd('create BaseModel')

        # Reset stdout
        sys.stdout = original_stdout

        # Check if an object is created and stored in FileStorage
        obj_id = sys.stdout.getvalue().strip()
        obj = self.fs.all()["BaseModel." + obj_id]
        self.assertTrue(obj is not None)

    def test_create_user_with_params(self):
        # Redirect stdout to capture console output
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()

        # Run the "create" command with parameters for a User instance
        self.console.onecmd('create User email="test@example.com" password="secret"')

        # Reset stdout
        sys.stdout = original_stdout

        # Check if an object is created and stored in FileStorage
        obj_id = sys.stdout.getvalue().strip()
        obj = self.fs.all()["User." + obj_id]
        self.assertTrue(obj is not None)
        self.assertEqual(obj.email, "test@example.com")
        self.assertEqual(obj.password, "secret")

    def test_create_place_with_params(self):
        # Redirect stdout to capture console output
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()

        # Run the "create" command with parameters for a Place instance
        self.console.onecmd('create Place name="My_little_house" number_rooms=4')

        # Reset stdout
        sys.stdout = original_stdout

        # Check if an object is created and stored in FileStorage
        obj_id = sys.stdout.getvalue().strip()
        obj = self.fs.all()["Place." + obj_id]
        self.assertTrue(obj is not None)
        self.assertEqual(obj.name, "My_little_house")
        self.assertEqual(obj.number_rooms, 4)

    def test_create_invalid_class(self):
        # Redirect stdout to capture console output
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()

        # Run the "create" command with an invalid class name
        self.console.onecmd('create InvalidClass')

        # Reset stdout
        sys.stdout = original_stdout

        # Check if an error message is printed
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_create_invalid_param_syntax(self):
        # Redirect stdout to capture console output
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()

        # Run the "create" command with invalid parameter syntax
        self.console.onecmd('create BaseModel name="Invalid"="Parameter"')

        # Reset stdout
        sys.stdout = original_stdout

        # Check if an error message is printed
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** value missing **")

if __name__ == '__main__':
    unittest.main()