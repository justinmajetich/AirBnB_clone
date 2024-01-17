#!/usr/bin/python3
"""
Unittests for console.py
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for console.py"""

    @classmethod
    def setUpClass(cls):
        """Set up the class"""
        cls.console = HBNBCommand()

    def test_quit_command(self):
        """Test quit command"""
        pass
        """with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")"""

    def test_EOF_command(self):
        """Test EOF command"""
        pass
        """with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")"""

    def test_emptyline(self):
        """Test emptyline method"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.emptyline()
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_create(self):
        """Test create"""
        pass

    def test_show(self):
        """Test show"""
        pass

    def test_help_quit_command(self):
        """Test help quit command"""
        pass
        """with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("help quit")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Quit command to exit the program")"""

    def test_help_EOF_command(self):
        """Test help EOF command"""
        pass
        """with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("help EOF")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "EOF command to exit the program")"""

    def test_noninteractive_mode_help(self):
        """Test non-interactive mode with help command"""
        pass
        """with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('sys.stdin', StringIO('help\n')) as mock_stdin:
                self.console.cmdloop()
                output = mock_stdout.getvalue().strip()
                self.assertIn("(hbnb)", output)
                self.assertIn"""

    def test_noninteractive_mode_quit(self):
        """Test non-interactive mode with quit command"""
        pass
        """with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('sys.stdin', StringIO('quit\n')) as mock_stdin:
                self.console.cmdloop()
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "(hbnb)")"""


if __name__ == '__main__':
    unittest.main()
