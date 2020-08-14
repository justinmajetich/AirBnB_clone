#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String


class Amenity(BaseModel):
    '''class Amenity'''

    __tablename__ = 'amenities'
    name = Column(String(128))
    place_amenities = relationship(
        "Place", secondary=place_amenity, backref='amenities')
