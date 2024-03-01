#!/usr/bin/python3
""" Tests for console.py """
import os
import unittest
import pycodestyle
from console import HBNBCommand


class TestConsoleClass(unittest.TestCase):
    """ Tests for the console class initialization and related operations """

    @classmethod
    def setUp(cls):
        """ Preparation method executed before each test """
        cls.konsol = HBNBCommand()

    @classmethod
    def tearDown(cls):
        """ Cleanup method executed after each test """
        try:
            os.remove("file.json")
        except IOError:
            pass
        del cls.konsol

    def test_HBNBCommand_docstring(self):
        """ Tests docstring for the HBNBCommand class """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_preloop_docstring(self):
        """ Tests docstring for the preloop method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.preloop.__doc__) > 0)

    def test_precmd_docstring(self):
        """ Tests docstring for the precmd method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.precmd.__doc__) > 0)

    def test_postcmd_docstring(self):
        """ Tests docstring for the postcmd method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.postcmd.__doc__) > 0)

    def test_do_quit_docstring(self):
        """ Tests docstring for the do_quit method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.do_quit.__doc__) > 0)

    def test_help_quit_docstring(self):
        """ Tests docstring for the help_quit method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.help_quit.__doc__) > 0)

    def test_do_EOF_docstring(self):
        """ Tests docstring for the do_EOF method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.do_EOF.__doc__) > 0)

    def test_help_EOF_docstring(self):
        """ Tests docstring for the help_EOF method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.help_EOF.__doc__) > 0)

    def test_emptyline_docstring(self):
        """ Tests docstring for the emptyline method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.emptyline.__doc__) > 0)

    def test_do_create_docstring(self):
        """ Tests docstring for the do_create method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.do_create.__doc__) > 0)

    def test_help_create_docstring(self):
        """ Tests docstring for the help_create method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.help_create.__doc__) > 0)

    def test_do_show_docstring(self):
        """ Tests docstring for the do_show method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.do_show.__doc__) > 0)

    def test_help_show_docstring(self):
        """ Tests docstring for the help_show method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.help_show.__doc__) > 0)

    def test_do_destroy_docstring(self):
        """ Tests docstring for the do_destroy method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.do_destroy.__doc__) > 0)

    def test_help_destroy_docstring(self):
        """ Tests docstring for help_destroy method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.help_destroy.__doc__) > 0)

    def test_do_all_docstring(self):
        """ Tests docstring for the do_all method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.do_all.__doc__) > 0)

    def test_help_all_docstring(self):
        """ Tests docstring for the help_all method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.help_all.__doc__) > 0)

    def test_do_count_docstring(self):
        """ Tests docstring for the do_count method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.do_count.__doc__) > 0)

    def test_help_count_docstring(self):
        """ Tests docstring for the help_count method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.help_count.__doc__) > 0)

    def test_do_update_docstring(self):
        """ Tests docstring for the do_update method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.do_update.__doc__) > 0)

    def test_help_update_docstring(self):
        """ Tests docstring for the help_update method of HBNBCommand class """
        self.assertTrue(len(HBNBCommand.help_update.__doc__) > 0)

    def test_pycodestyle_compliance(self):
        """ Test if the code adheres to the PEP 8 style guidelines. """
        style_checker = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style_checker.check_files(['console.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_HBNBCommand_object_type(self):
        """Verify that the type function returns the correct object type. """
        konsol = HBNBCommand()
        self.assertEqual(type(konsol), HBNBCommand)
        self.assertTrue(isinstance(konsol, HBNBCommand))


if __name__ == "__main__":
    unittest.main()
