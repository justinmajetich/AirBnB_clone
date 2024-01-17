#!/usr/bin/python3
""" State Module for HBNB project """
import uuid
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
    def __init__(self, *args, **kwargs):
        """ Initializes a new State instance """
        super().__init__(*args, **kwargs)
        if not kwargs.get('id'):
            self.id = str(uuid.uuid4())
