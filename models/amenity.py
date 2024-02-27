#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from .base_model import Base
from sqlalchemy import Column, String
import os
storage_type = os.getenv('HBNB_TYPE_STORAGE', 'file')


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column('name', String(128), nullable=False)
    else:
        name = ""
