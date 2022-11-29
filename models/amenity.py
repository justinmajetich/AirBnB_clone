#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    __tablename__ = 'Amenities'
    name = Column(String(128), nullable=False)
