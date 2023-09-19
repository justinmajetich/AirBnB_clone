#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    name = Column('name', String(128), nullable=False)
    __tablename__ = 'amenities'
    place_amenities = relationship('Place', secondary=place_amenity)
