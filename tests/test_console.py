#!/usr/bin/python3
#!/usr/bin/python3
"""module for testing airbnb clone console"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import console
import sys


class TestConsole(unittest.TestCase):
    """class for testing console of airbnb clone"""

    console = console.HBNB.Command()

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        jfile= "file.son"
        if os.path.exists(jfile):
            os.remove(jfile)

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_prompt(self):
        """test that the prompt is correct"""
        self.assertEqual(self.console.prompt, '(hbnb) ')

    def test_do_quit(self):
        with self.assertRaises(SystemExit):
            self.console.do_quit()

    def test_do_EOF(self):
        with self.assertRaises(SystemExit):
            self.console.do_EOF()

    def test_do_create(self):
        self.console.User.create(potato="yes")
        with open("file.json", "r") as file:
            self.assertEqual(file.read(), "test")