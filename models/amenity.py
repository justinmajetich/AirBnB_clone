#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """The Amenity class, contains amenity name"""
    if dbstorage == 'db':
        __tablename__ = 'amenties'
        name = Column(String(128), nullable=False)
    else:
        name = ""
