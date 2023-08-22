#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storage_type
from sqlalchemy import Column, String


class Amenity(BaseModel):
    """Defines the amenity class"""
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
