#!/usr/bin/python3
"""Unit tests for the State class."""

# Importing necessary modules
from tests.test_models.test_base_model import test_basemodel
from models.state import State

class TestStateAttributes(test_basemodel):
    """Test cases for the attributes of the State class."""
    
    def __init__(self, *args, **kwargs):
        """Initialize test cases."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_type(self):
        """Test if the 'name' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.name), str)
