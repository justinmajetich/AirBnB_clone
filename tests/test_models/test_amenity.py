#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    Define extra tests for Amenity class which inherits from the BaseModel \
class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of the class test
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Ensure that the `name` attribute of the Amenity class is a string
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
