#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class Amenity(BaseModel, Base):
    """ Amenity class to store amenity information """
    __tablename__ = "amenities"

    name = Column(
            String(128), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    place_amenities = relationship("Place", secondary="place_amenity",
                                   backref="amenities", viewonly=False)
    def __init__(self, *args, **kwargs):
        """This method happens as soon as a instance is created"""
        super().__init__(*args, **kwargs)
