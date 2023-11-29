#!/usr/bin/python3
from models.base_model import BaseModel
"""
Module class: City
"""


class City(BaseModel):
    """definition for class City"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(self, *args, **kwargs)
