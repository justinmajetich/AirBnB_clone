#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
from contextlib import redirect_stdout
import inspect
import io
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")


class TestConsoleCommands(unittest.TestCase):
    """Class to test functionality of console commands"""
    @classmethod
    def setUpClass(cls):
        """Create command console to test with"""
        cls.cmdcon = HBNBCommand()

    def setUp(self):
        """Create in memory buffer to capture stdout"""
        self.output = io.StringIO()

    def tearDown(self):
        """Close in memory buffer after test completes"""
        self.output.close()

    def test_do_create(self):
        """Test do_create method of console"""
        with redirect_stdout(self.output):
            self.cmdcon.onecmd('create')
            self.assertEqual(self.output.getvalue(),
                             "** class name missing **\n")
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create blah')
            self.assertEqual(self.output.getvalue(),
                             "** class doesn't exist **\n")
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create State')
            self.assertRegex(self.output.getvalue(),
                             '[a-z0-9]{8}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{12}')
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create State name="California"')
            self.assertRegex(self.output.getvalue(),
                             '[a-z0-9]{8}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{12}')
