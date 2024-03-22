#!/usr/bin/python3
"""
Unit tests for the console module
"""
import unittest
import sys
import io
from contextlib import contextmanager
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


@contextmanager
def captured_output():
    """
    Context manager to capture stdout and stderr
    """
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestConsole(unittest.TestCase):
    """
    Test cases for the Console class
    """

    def setUp(self):
        """
        Set up test environment
        """
        self.console = HBNBCommand()
        self.test_obj = BaseModel()
        storage.new(self.test_obj)
        storage.save()

    def tearDown(self):
        """
        Tear down test environment
        """
        storage.delete(self.test_obj)
        storage.save()

    def test_create(self):
        """
        Test the create command
        """
        with captured_output() as (out, err):
            self.console.onecmd("create BaseModel")
        obj_id = out.getvalue().strip()
        self.assertIn(obj_id, storage.all().keys())

    def test_show(self):
        """
        Test the show command
        """
        with captured_output() as (out, err):
            self.console.onecmd("show BaseModel {}".format(self.test_obj.id))
        expected_output = str(self.test_obj)
        self.assertEqual(out.getvalue().strip(), expected_output)

    def test_all(self):
        """
        Test the all command
        """
        with captured_output() as (out, err):
            self.console.onecmd("all BaseModel")
        expected_output = [str(self.test_obj)]
        self.assertEqual(out.getvalue().strip(), str(expected_output))

    def test_destroy(self):
        """
        Test the destroy command
        """
        with captured_output() as (out, err):
            self.console.onecmd("destroy BaseModel {}".format(self.test_obj.id))
        self.assertNotIn(self.test_obj.id, storage.all().keys())


if __name__ == "__main__":
    unittest.main()
