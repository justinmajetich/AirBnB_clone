#!/usr/bin/python3
""" State Module for HBNB project, Defines Amenity CLass """
from models.base_model import BaseModel, Base, Column, String


class Amenity(BaseModel, Base):
    """Represents amenity.
    Attributes:
        __tablename__ (str): Name of the table
        name (str): The name of amenity.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
