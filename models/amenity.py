#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''Amenity class'''
    __tablename__ = "amenities"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.place import place_amenity
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary=place_amenity, back_populates="amenities")

    def __init__(self, *args, **kwargs):
        '''initializes Amenity'''
        super().__init__(*args, **kwargs)
