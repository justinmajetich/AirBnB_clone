#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__()
        self.name = kwargs.get('name', "")
        
