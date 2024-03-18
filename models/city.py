#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from . import storage
import uuid

class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = kwargs.get('id', str(uuid.uuid4()))
        City.state_id = kwargs.get('state_id', City.state_id)
        City.name = kwargs.get('name', City.name)
        storage.new(self)
