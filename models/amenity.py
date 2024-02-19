#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models import type_of_storage


class Amenity(BaseModel, Base):
    '''Class for Amenities'''

    __tablename__ = 'amenities'

    if type_of_storage == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ''
