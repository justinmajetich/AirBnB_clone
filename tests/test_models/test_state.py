#!/usr/bin/python3
from tests.test_models.test_base_model import test_basemodel
from models.state import State

class TestState(test_basemodel):
    """Test class for State"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_attributes(self):
        """Test that attributes are correctly set"""
        state = self.value()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_to_dict(self):
        """Test the to_dict method"""
        state = self.value()
        state.name = "California"
        state_dict = state.to_dict()
        self.assertEqual(state_dict['name'], "California")
        self.assertIn('__class__', state_dict)

    def test_str(self):
        """Test the __str__ method"""
        state = self.value()
        state.name = "California"
        string = state.__str__()
        self.assertIn("[State]", string)
        self.assertIn("'name': 'California'", string)