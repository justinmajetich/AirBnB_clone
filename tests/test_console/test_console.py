import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up testing environment"""
        self.console = HBNBCommand()

    def test_do_create_valid_class_name(self):
        """Test creating an object with valid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue()
            # Here you should check that the output matches the expected value.
            # This could be the id of the new object, or some other output from the method.

    def test_do_create_invalid_class_name(self):
        """Test creating an object with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create NonExistentClass")
            output = f.getvalue()
            # Here you should check that the output matches the expected value.
            # This could be an error message, or some other output from the method.

    def test_do_create_valid_parameter(self):
        """Test creating an object with valid parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create User first_name="John" last_name="Doe" age=30')
            output = f.getvalue()
            # Here you should check that the output matches the expected value.
            # This could be the id of the new object, or some other output from the method.

    def test_do_create_invalid_parameter(self):
        """Test creating an object with invalid parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create User first_name John last_name Doe age 30')
            output = f.getvalue()
            # Here you should check that the output matches the expected value.
            # This could be an error message, or some other output from the method.
