#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skip("No state_id added")
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_state_id_in_city(self):
        """Test if state_id is present """
        new = self.value()
        new.state_id = "7jfjf0jc-3aab-j5j5-j2j1-1jaj8j8jjj77"
        self.assertEqual(type(new.state_id), str)

    @unittest.skip("No name added")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_name_of_city(self):
        """ """
        new = self.value()
        new.name = "San Francisco"
        self.assertEqual(type(new.name), str)
