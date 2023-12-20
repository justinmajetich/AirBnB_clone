#!/usr/bin/python3
"""
Writing some tests for the console
"""
import unittest
import sqlalchemy
import json
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
# from models.base_model import BaseModel
# from models.user import User


def clear_stream(st):
    print(st)


class TestConsole(unittest.TestCase):
    """Represents the test class for the HBNBCommand class.
    """

    def get_console(self, command):
        """Method for getting the console"""
        with patch('sys.stdout', new=StringIO()) as cons_out:
            cons = HBNBCommand()
            cons.onecmd(command)
            return cons_out.getvalue().strip()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == "db",
                     "only available in the filestorage")
    def test_fs_create(self):
        """Testing the new create features"""
        output = self.get_console('create City name="Texas"')
        self.assertIn(f'City.{output}', storage.all().keys())

    def test_fs_create_show(self):
        with patch('sys.stdout', new=StringIO()) as cons_out:
            cons = HBNBCommand()

            cons.onecmd('create Place name="Center" num="00001" max_guest=10 lat=127.2345')
            _id = cons_out.getvalue().strip()

            cons.onecmd(f"show Place {_id}")
            show_out = cons_out.getvalue().strip()
            self.assertIn("'name': 'Center'", show_out)
            self.assertIn("'max_guest': 10", show_out)
            self.assertIn("'lat': 127.2345", show_out)
            self.assertIn("'num': '00001'", show_out)
