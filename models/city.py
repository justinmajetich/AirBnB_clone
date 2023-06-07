#!/usr/bin/python3
"""
Define the ``City`` class that inherits from the class ``BaseModel``
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Define the class City
    """
    state_id = str()    # it will be State.id
    name = str()
