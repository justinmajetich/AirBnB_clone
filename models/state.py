#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
    valid_attr = ['name']

    def __init__(self, *args, **kwargs):
        super(State, self).__init__()
        for key in self.valid_attr:
            if key in kwargs:
                setattr(self, key, kwargs[key])
