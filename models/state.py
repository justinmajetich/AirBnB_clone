#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from datetime import datetime


class State(BaseModel):
    """ 
    State class
    need to explicitly declare updated_at and created_at
    because to_dict is overriding the to_dict in BaseModel
    """
    created_at = datetime.now()
    updated_at = datetime.now()
    def __init__(self, *args, **kwargs):
        """ Initializes a new instance of State """
        super().__init__(*args, **kwargs)
        self.name = ""

    def to_dict(self):
        """Convert instance into dict format, including the name attribute"""
        dictionary = super().to_dict()
        dictionary['name'] = self.name
        return dictionary
