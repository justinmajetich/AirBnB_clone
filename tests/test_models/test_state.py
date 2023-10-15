#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import pep8


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
        self.assertEqual(type(new), self.value)

     def test_pep8_conformance_state(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_class(self):
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_father(self):
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_state(self):
        """
        Test attributes of Class State
        """
        my_state = State()
        my_state.name = "Antioquia"
        self.assertEqual(my_state.name, 'Antioquia')
