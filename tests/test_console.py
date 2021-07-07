#!/usr/bin/python3
''' Class Test '''
import unittest
import pep8
import inspect
import datetime
import os
from console import HBNBCommand


class console_test(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


    def do_create_test(self):
        """Tests the do_create function"""
        return HBNBCommand()