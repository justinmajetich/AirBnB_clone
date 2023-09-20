#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os


place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
                primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
                primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay 
        Inherit from BaseModel and Base class
    """

    __tablename__ = 'places'
    
    if(os.getenv("HBNB_TYPE_STORAGE") == 'db'):
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0,  nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        amenities = relationship('Amenity', secondary="place_amenity",
                viewonly=False)
        reviews = relationship('Reviews', cascade='all, delete', backref='place')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
