#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
    def __init__(self, *args, **kwargs):
        """ Set up an instance with its properties. """
        super().__init__(*args, **kwargs)
