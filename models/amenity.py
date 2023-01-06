#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import Place_amenity


class Amenity(BaseModel):
    """This is the class for amenity
    attributes:
        name = ""
    """
    __tablename__ =  "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
