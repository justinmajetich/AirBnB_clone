#!/usr/bin/python3
"""console"""
import unittest
import console



class test_the_console(unittest.TestCase):
    """test the console"""
    def test_console(self):
        """test the console"""
        self.assertIsNotNone(console.__doc__)