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
