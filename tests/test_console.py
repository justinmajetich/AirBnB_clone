#!/usr/bin/python3
"""Unittests to test main console functionality
"""
import os
import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test module for console functionality
    """
    @classmethod
    def setUp(cls):
        """Setup that clears 'file.json' and creates instance
        of command console """
        if os.path.exists("file.json"):
            os.remove("file.json")
        # create new file.json in append mode
        open("file.json", "a").close()
        # create instance of HBNBCommand
        cls.console = HBNBCommand()

    def test_docstring(self):
        """Test that looks for docstring for each console method
        """
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.preloop.__doc__)
        self.assertIsNotNone(HBNBCommand.precmd.__doc__)
        self.assertIsNotNone(HBNBCommand.postcmd.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.help_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.help_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.help_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.help_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.help_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.help_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.help_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.help_update.__doc__)


if __name__ == '__main__':
    unittest.main()
