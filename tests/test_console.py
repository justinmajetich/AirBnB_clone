#!/usr/bin/python3
"""Module that holds the test for hbnb console
    """
import unittest
import pep8
import console
from io import StringIO
from unittest.mock import patch

hbnb_console = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """Unit test class for console tests

    Args:
        unittest ([class]): Testcase
    """

    def test_console_pep8(self):
        """Check pep8 on console
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./console.py"])
        self.assertEqual(result.total_errors, 0)

    def test__test_file_console_pep8(self):
        """Check pep8 on test console
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./tests/test_console.py"])
        self.assertEqual(result.total_errors, 0)

    def test_console_docstring(self):
        """Check docstring console
        """
        self.assertIsNot(console.__doc__, None,
                         "console.py without documentation")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py without documentation")

    def test_class_console_docstring(self):
        """Check docstring test console
        """
        self.assertIsNot(hbnb_console.__doc__, None,
                         "HBNBCommand without documentation")
        self.assertTrue(len(hbnb_console.__doc__) >= 1,
                        "HBNBCommand without documentation")

    def test_prompt(self):
        """Test console prompt
        """
        self.assertEqual("(hbnb) ", hbnb_console.prompt)

    def test_to_create(self):
        """test to create updated method
        """
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb_console().onecmd("create BaseModel")
            f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            hbnb_console().onecmd("create BaseModel")
            f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            hbnb_console().onecmd('create State name="California"')
            f.getvalue().strip()
