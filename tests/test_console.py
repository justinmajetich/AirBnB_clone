#!/usr/bin/python3
"""
tests the Console Docs of the Class TestConsoleDocs
"""

import console
import inspect
import pep8
import unittest
HBNB COMMAND = console.HBNBCommand


class TestConsoleDocs(unittest.Testcase):
	"""tests check the documentation of the console"""
	def test_pep8_conformance_console(self):
		pepe8s = pepe8.StyleGuide(quiet=True)
		result = pep8s.check_files(['console.py'])
		self.assertEqual(result.total_errors, 0, "Found code style errors (and warnong).")


	def test_pep8_conformance_test_console(self):
	"""checks that the tests/tests_console.py conforms to pep8."""
		 pepe8s = pepe8.StyleGuide(quiet=True)
                result = pep8s.check_files(['tests/test_console.py'])
                self.assertEqual(result.total_errors, 0, "Found code style errors (and warnong).")

	def test_console_module_dicstring(self):
	"""test for console.py module docstring"""
		self.assertIsNot(console.__doc__, None, "console.py needs a docstring")
		self.assertTrue(len(console.__doc__) >= 1, "cosole.py needs a docstring")


	def test_HBNBCommand_class_docstring(self):
		self.assertIsNot(HBNBCommand.__doc__, None, "HBNBCommand class needs a docstring")
		self.assertTrue(len(HBNBCommand.__doc__) >= 1, "HBNBCommand class needs a docstring")
