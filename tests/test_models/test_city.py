#!/usr/bin/python3
""" """
from unittest.case import skipIf
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
import os


class test_City(test_basemodel):
    """class test City """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_state_id(self):
        """ """
        new = self.value()
        new.state_id = "Toto"
        self.assertIn("'state_id': '{}'".format(new.state_id), str(new))
        # self.assertEqual(type(new.state_id), str)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_name(self):
        """ """
        new = self.value()
        new.name = "San Francisco"
        self.assertIn("'name': '{}'".format(new.name), str(new))
        # self.assertEqual(type(new.name), str)
