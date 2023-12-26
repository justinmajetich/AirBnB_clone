#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """ Amenity class """
    name = ""
