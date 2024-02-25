#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sys

class State(BaseModel):
    """ State class """
    name = ""
    if 'id' not in kwargs:
        self.id = str(uuid4())
