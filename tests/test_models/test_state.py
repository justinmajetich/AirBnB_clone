#!/usr/bin/python3
""" """
from unittest.case import skipIf
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import os


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_name3(self):
        """ """
        new = self.value()
        new.name = "toto"
        self.assertIn("'name': '{}'".format(new.name), str(new))
        # self.assertEqual(type(new.name), str)
