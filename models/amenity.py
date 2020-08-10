#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ The Amenity class, contains name """
    name = ""
    valid_attr = ['name']

    def __init__(self, *args, **kwargs):
        super(Amenity, self).__init__()
        for key in self.valid_attr:
            if key in kwargs:
                setattr(self, key, kwargs[key])
