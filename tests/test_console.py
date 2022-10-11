!#/usr/bin/python3

"""
contains class TestConsoleDoc
"""

import console
import inspect
import unittest
HBNBCommand=console.HBNBCommand

class TestConsole(unittest.TestCase):

	def test_HBNBCommand_class_docstring(self):
		"""Test for the HBNBCommand class doc"""
		self.assertIsNot(HBNBCommand.__doc__,None,"HBNBCommand class needs a docstring")
		self.assertTrue(len(HBNBCommand.__doc__)>=1,"HBNBCommand class needs a docstring")