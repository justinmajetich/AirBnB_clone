#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""
