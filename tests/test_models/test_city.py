#!/usr/bin/python3
"""
Importing modules containing uni test for city class
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """
    Test case for city class inheriting from Basemodel
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for test cases
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test case for checking ype of state_id attribute in city
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Test Case for checking type of name attribute in City
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
