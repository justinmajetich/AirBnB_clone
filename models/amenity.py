#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class Amenity(BaseModel):  #don't forget to add Base to the function Amenity(BaseModel, Base) 
    name = ""
