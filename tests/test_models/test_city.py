#!/usr/bin/python3
"""
unittest module to test the City class
"""
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class test_City(TestBaseModel):
    """
    Unittest subclass to test the City Class
    """

    def __init__(self, *args, **kwargs):
        """
        init the City calss and its super
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test the City state_id atrribute"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test the City name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
