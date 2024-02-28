#!/usr/bin/python3
""" Module for running test cases """
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os


class test_console(unittest.TestCase):
    """Test module for the console"""

    @classmethod
    def setUpClass(cls):
        """HBNBCommand testing setup.

        Temporarily rename any existing file.json.
        Reset FileStorage objects dictionary.
        Create an instance of the command interpreter.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    def test_quit(self):
        """Test quit command input."""
        with patch('builtins.exit') as mock_exit:
            with patch("sys.stdout", new=StringIO()) as f:
                self.HBNB.onecmd("quit")
                mock_exit.assert_called_once()
                self.assertEqual("", f.getvalue())

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)


if __name__ == "__main__":
    unittest.main()
