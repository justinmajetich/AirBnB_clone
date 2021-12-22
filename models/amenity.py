#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Manage the amenities of the places"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
