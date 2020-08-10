#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
    valid_attr = ['state_id', 'name']

    def __init__(self, *args, **kwargs):
        super(City, self).__init__()
        for key in self.valid_attr:
            if key in kwargs:
                setattr(self, key, kwargs[key])
