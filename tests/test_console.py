#!/usr/bin/python3
""" test_console module """

import unittest
import datetime
from uuid import UUID
import json
import os
from os import getenv
from unittest.mock import patch
from io import StringIO
import MySQLdb
import pep8
import tests
import console
from console import HBNBCommand
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


class test_console(unittest.TestCase):
    """ test_console class """

    def __init__(self, *args, **kwargs):
        """ __init__ function """
        super().__init__(*args, **kwargs)
        self.name = 'HBNBCommand'
        self.console = HBNBCommand()
        if getenv('HBNB_TYPE_STORAGE') == "db":
            self.db = MySQLdb.connect(user=os.environ.get('HBNB_MYSQL_USER'),
                                      passwd=os.environ.get('HBNB_MYSQL_PWD'),
                                      db=os.environ.get('HBNB_MYSQL_DB'),
                                      port=3306,
                                      host=os.environ.get('HBNB_MYSQL_HOST'))

    def setUp(self):
        """ setUp function """
        pass

    def tearDown(self):
        """ removing file.json created and closing DB connection """
        if os.access("file.json", os.F_OK):
            os.remove("file.json")
        if getenv('HBNB_TYPE_STORAGE') == "db":
            self.db.close()

    def test_pep8_style(self):
        """ Checking pep8 coding style """
        style = pep8.StyleGuide(quiet=True)
        output = style.check_files(["console.py"])
        self.assertEqual(output.total_errors, 0, 'fix Pep8')

    def test_doctstrings(self):
        """ Checking docstring existance """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """ Checking correct output on empty line """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(' ')
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """ Testing the create command """
        if(os.getenv("HBNB_TYPE_STORAGE") != "db"):
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd('create State')
                s = f.getvalue()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd('all State')
                self.assertEqual('["[State]', f.getvalue()[:9])
            self.console.onecmd("destroy State " + s)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Parcero")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

        s = ""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="AjaLandia"')
            s = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all State")
            out = f.getvalue()
            self.assertEqual('["[State]', out[:9])
            self.assertIn("AjaLandia", out)

        self.console.onecmd("destroy State " + s)
