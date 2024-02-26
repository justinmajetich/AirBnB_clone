#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from .base_model import Base
from .place_amenities import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column('name', String(128), nullable=False)
    places = relationship('Place', secondary=place_amenity, back_populates='amenities')
