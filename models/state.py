#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from . import storage
import uuid

class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        State.name = kwargs.get('name', State.name)
        super().__init__(*args, **kwargs)
        storage.new(self)

