#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Ameniy"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__()
