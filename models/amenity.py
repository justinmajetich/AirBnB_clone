#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place_amenity import place_amenity

class Amenity(BaseModel, Base):
    """ A Amenity to stay """
    __tablename__ = 'amenities'
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place",
                                   secondary=place_amenity,
                                   back_populates="amenities",
                                   viewonly=False)
