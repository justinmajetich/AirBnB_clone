#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import sys


""" This module the test cases for different
for the console that we built already"""


class TestConsole(unittest.TestCase):
    """This class contains several testcases of
    the console features and other associated features"""

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_create_params(self):
        """Method to test the create function..."""
        with patch('sys.stdout', new=StringIO()) as f:
            test_cmd_line = 'create User name="Fasasi1"   address_no=44\
                            balance=3.14 quotes="The_dog_is_\"lazy"'
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            obj_id = f.getvalue()
            f.seek(0)
            f.truncate(0)
            test_cmd_line = 'show User {}'.format(obj_id)
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            result = f.getvalue()
            regex = "'name': 'Fasasi1'"
            self.assertRegex(result.strip(), regex)
            regex = "'address_no': 44"
            self.assertRegex(result.strip(), regex)
            regex = "'balance': 3.14"
            self.assertRegex(result.strip(), regex)
            regex = 'quotes\': \'The dog is "lazy\''
            self.assertRegex(result, regex)
            f.seek(0)
            f.truncate(0)
