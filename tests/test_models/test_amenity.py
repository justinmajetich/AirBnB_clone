#!/usr/bin/python3
"""
testing amenity
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ testing amenity classs
    """

    def __init__(self, *args, **kwargs):
        """
        init for test amenity
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        test_name2 test
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
