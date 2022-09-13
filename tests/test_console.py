#!/usr/bin/python3
"""This module defines a test suite for the console module"""

import os
import pep8
import unittest
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for testing the HBNB command intepreter"""

    @classmethod
    def setUpClass(cls):
        """HBNBCommand test setup
        This function temporarily renames the file.json
        to tmp, to prevent our test cases from intefering
        with application data stored in the file
        It also creates an instance of HBNBCommand cmd
        """
        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass
        cls.hbnb_cmd = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """HBNBCommand test teardown/cleanup
        This function renames the tmp file to file.json
        so that the application can acces its previous data.
        It also deletes the HBNBCommand Instance
        """
        try:
            os.rename('tmp', 'file.json')
        except IOError:
            pass
        del cls.hbnb_cmd

    def setUp(self):
        """Reset Filestorage objects dictionary"""
        FileStorage._FileStorage__file_path = {}

    def tearDown(self):
        """Delete any json file created by the tests"""
        try:
            os.remove('file.json')
        except IOError:
            pass

    def test_pep8_conformance(self):
        """Test that code style conforms to pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(
                ['console.py']
                )
        self.assertEqual(result.total_errors, 0, 'Found code style errors')

    def test_docstrings(self):
        """Check for docstrings"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_create_with_parameters(self):
        """Check that create works properly when provided with parameters
        that are extra attributes of the object it creates"""
        # TODO: Add test logic
        pass

    def test_create_without_parameters(self):
        """Check that the create <classname> command works properly and
        creates an object of <classname>"""
        # TODO: Add test logic
        pass



