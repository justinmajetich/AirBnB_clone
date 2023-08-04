#!/usr/bin/python3
"""
Test File for Console
"""
import unittest
import pep8


class tests_Console(unittest.TestCase):
    """Unittest"""

    def test_pep8_conformance(self):
        """test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")
