#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
from models.state import State
from console import HBNBCommand
import os


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
        

        """ """
        class TestState(unittest.TestCase):
            """ """

            def setUp(self):
                """ """
                self.console = HBNBCommand()

            def tearDown(self):
                """ """
                del self.console

            def test_create_state(self):
                """ """
                # Get the number of current records in the table states
                initial_count = len(State.all())

                # Execute the console command
                self.console.onecmd("create State name=\"California\"")

                # Get the number of current records in the table states again
                final_count = len(State.all())

                # Check if the difference is +1
                self.assertEqual(final_count - initial_count, 1)

        if __name__ == '__main__':
            unittest.main()
