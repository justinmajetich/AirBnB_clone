#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
from models.base_model import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey, Float, Table
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
