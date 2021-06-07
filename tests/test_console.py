#!/usr/bin/python3

"""
Unittesting for console in interactive and non-interacitve
"""

import unittest
import os
from models.base_model import BaseModel
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class test_console(unittest.TestCase):
    """Console unit tests"""
    import models
    fs = models.storage

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE"), "FileStorage")
    def test_create_state(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        with patch('sys.stdout', new=StringIO()) as boy:
            HBNBCommand().onecmd("create State")
            state_id = boy.getvalue()[:-1]
        with open(fs._FileStorage__file_path, 'r') as guy:
            self.assertIn(state_id, guy.read())
