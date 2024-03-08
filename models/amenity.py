#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
import os
from models.base_model import BaseModel, Base

storage_type = os.getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column('name', String(128), nullable=False)
    else:
        name = ""
