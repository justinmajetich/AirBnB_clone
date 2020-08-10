#!/usr/bin/python3
""" test_console module """

import unittest
import datetime
from uuid import UUID
import json
import os
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.state import State


class test_console(unittest.TestCase):
    """ test_console class """

    def __init__(self, *args, **kwargs):
        """ __init__ function """
        super().__init__(*args, **kwargs)
        self.name = 'HBNBCommand'
        self.console = HBNBCommand()

    def setUp(self):
        """ setUp function """
        pass

    def test_create(self):
        """ Testing the create command """
        self.console.onecmd('create State name="California"')
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('all State')
            self.assertEqual('["[State]', f.getvalue()[:9])
