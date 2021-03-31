import unittest
import json
import models
import pep8
from models.base_model import BaseModel
from datetime import datetime


class TestConsole(unittest.TestCase):
    """ Unit test class for Base Model class """
    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_base_model(self):
        """Test that tests/test_models/test_base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(["tests/test_console.py"])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = TestConsole.__init__.__doc__
        self.assertGreater(len(doc), 1)
