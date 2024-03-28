#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ amenity class with name of amenity and relation with place"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
