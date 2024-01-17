#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__()

        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)
