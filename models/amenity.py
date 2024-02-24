#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
#vvv to be reimplimented
#from .base_model import Base
#from .place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


#vvv to be reimplimented
#class Amenity(BaseModel, Base):
class Amenity(BaseModel):
    __tablename__ = 'amenities'
    name = Column('name', String(128), nullable=False)
    #places = relationship('Place', secondary=place_amenity, back_populates='place_amenities')
