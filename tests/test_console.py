#!/usr/bin/python3
"""Unit Tests for console.py
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb = HBNBCommand()
        self.mock_stdout = StringIO()
        self.patched_stdout = patch("sys.stdout", self.mock_stdout)

    def tearDown(self):
        self.mock_stdout.close()
        self.patched_stdout.stop()
        storage._FileStorage__objects = {}

    def test_create(self):
        with self.patched_stdout:
            self.hbnb.onecmd("create BaseModel")
            self.assertTrue(
                isinstance(
                    storage.all()[
                        "BaseModel." + self.mock_stdout.getvalue().strip()
                        ],
                    BaseModel,
                )
            )

    def test_show(self):
        with self.patched_stdout:
            self.hbnb.onecmd("create BaseModel")
            self.hbnb.onecmd("show BaseModel "
                             + self.mock_stdout.getvalue().strip())
            self.assertTrue(
                self.mock_stdout.getvalue()
                .strip() != "** no instance found **"
            )

    def test_destroy(self):
        with self.patched_stdout:
            self.hbnb.onecmd("create BaseModel")
            self.hbnb.onecmd("destroy BaseModel "
                             + self.mock_stdout.getvalue().strip())
            self.assertTrue(self.mock_stdout.getvalue().strip() != "")

    def test_all(self):
        with self.patched_stdout:
            self.hbnb.onecmd("create BaseModel")
            self.hbnb.onecmd("all BaseModel")
            self.assertTrue(self.mock_stdout.getvalue().strip() != "[]")


if __name__ == "__main__":
    unittest.main()
