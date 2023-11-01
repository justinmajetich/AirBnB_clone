#!/usr/bin/python3
# KASPER edited 8:43 pm
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        x = State(name="Oklahoma")
        the_id = x.id
        new = City(name='Tulsa', state_id=the_id)
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        x = State(name="Oklahoma")
        the_id = x.id
        new = City(name='Tulsa', state_id=the_id)
        self.assertEqual(type(new.name), str)
