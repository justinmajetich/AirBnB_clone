#!/usr/bin/python3
"""
Define the ``Amenity`` class that inherits from the class ``BaseModel``
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Define the class Amenity
    """
    name = str()
