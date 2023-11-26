#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models import hbnb_type_storage


class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    if hbnb_type_storage == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
