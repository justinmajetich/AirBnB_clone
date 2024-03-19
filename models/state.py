#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, **kwargs):
        super().__init__()
        for key, value in kwargs.items():
            if hasattr(self, key) and key != '__class__':
                attr_type = type(getattr(self, key))
                # Convert value to the appropriate type
                if attr_type == int:
                    value = int(value)
                elif attr_type == float:
                    value = float(value)
                setattr(self, key, value)
