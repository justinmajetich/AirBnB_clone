import unittest
from unittest.mock import patch
import sys
from console import HBNBCommand
from io import StringIO
from test_models import test_base_model

class ConsoleTestCase(unittest.TestCase):
    def setUp(self):
        '''set up test dependants'''
        self.console = HBNBCommand()

    def tearDown(self):
        '''cleanup test'''

    def test_help_command(self):
        '''testing the help command'''

        output = self.console.onecmd("help")

        expected_output = self.assertEqual(output.strip(), expected_output.strip())

    def test_help_invalid_command(self):
        '''test help w invalid command'''
        output = self.console.onecmd("help invalid")

        expected_output = "*** No help on invalid"
        self.assertEqual(output.strip(), expected_output.strip())

    def test_quit_command(self):
        '''tests quit cmd'''
        captured_output = StringIO()

        sys.stdout = captured_output
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        expected_output = self.assertEqual(output, expected_output)

    def test_create_command(self):
        '''test create cmd'''
        captured_output = StringIO()

        sys.stdout = captured_output

        self.console.onecmd(test_base_model)

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()

        object_id = 
        expected_output = object_id
        self.assertEqual(output, expected_output)

if __name__ == '-_main__':
    unittest.main()