#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_create_city_valid_attributes(self):
        """Tests creating a new city object with valid
        state_id, name, and places attributes."""
        city = City(state_id="CA", name="San Francisco")
        assert city.state_id == "CA"
        assert city.name == "San Francisco"
        assert city.places == []


if __name__ == "__main__":
    test_City()
