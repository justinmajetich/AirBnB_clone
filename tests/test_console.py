#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittestcd
import datetimecd
from uuid import UUID
import json
import os
import pep8
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestHBCommand(unittest.TestCase):
    """Test for command line"""

    def test_style(self):
        """test pep8 style"""
        style = pep8.StyleGuide()
        m = style.check_files(["console.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_quit(self, command):
        """ Method to exit the HBNB console"""
        pass

    def test_docstring(self):
        """ """

    def test_help_EOF(self):
        """ Prints the help documentation for quit  """
        pass

    if getenv("HBNB_TYPE_STORAGE") != "db":

        def test_show(self, arg):
            """ Handles EOF to exit program """
            pass

        def test_create(self):
            """ Prints the help documentation for EOF """
            pass

        def test_count(self):
            """ """
            pass

        def test_destroy(self, args):
            """ Destroys a specified object """
            pass

        def test_update(self, args):
            """ Updates a certain object with new info """
            pass

        def test_help_all(self, args):
            """ Shows all objects, or all objects of a class"""
            pass
