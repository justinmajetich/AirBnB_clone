#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from models import storage_type
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
=======
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
>>>>>>> f375e0cd1889c516746ec76f071c7bed658c682c
