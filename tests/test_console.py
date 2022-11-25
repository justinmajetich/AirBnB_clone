#!/usr/bin/python3
"""test for console"""
import unittest
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Class to test console"""

    def test_documentation(self):
        """Testing module docstring"""
        self.assertTrue(console.__doc__)
        self.assertTrue(console.HBNBCommand.__doc__)

    def test_methods_doc(self):
        """Testing all docstring of all methods"""
        for all_methods in dir(HBNBCommand):
            self.assertTrue(all_methods.__doc__)


if __name__ == '__main__':
    unittest.main()
