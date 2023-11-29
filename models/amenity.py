#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
