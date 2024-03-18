#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from . import storage
import uuid

class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Amenity.name = kwargs.get('name', Amenity.name)
        
