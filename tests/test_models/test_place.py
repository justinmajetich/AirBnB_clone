#!/usr/bin/python3
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class TestPlace(test_basemodel):
    """Test class for Place"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place