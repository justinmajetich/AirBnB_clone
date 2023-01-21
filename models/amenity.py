#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models import dbstorage


class Amenity(BaseModel, Base):
    """The Amenity class, contains amenity name"""
    __tablename__ = "amenities"
    if dbstorage == 'db':    
        name = Column(String(128), nullable=False)
    else:
        name = ""
