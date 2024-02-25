#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sys

class State(BaseModel):
    """ State class """
    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'id' not in kwargs:
            self.id = str(uuid4())
