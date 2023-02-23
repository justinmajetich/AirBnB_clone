#!/usr/bin/python3
""" Place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import os


place_amenity = Table('place_amenity',Base.metadata,
                          column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel):
    """ A place to stay """
    __tablename__= 'places'

    city_id = column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = column(String(60), ForeignKey('user_id'), nullable=False)
    name = column(String(128), nullable=False)
    description = column(String(1024), nullable=True)
    number_rooms = column(Integer, default=0, nullable=False)
    number_bathrooms = column(Integer, default=0, nullable=False)
    max_guest = column(Integer, default=0, nullable=False)
    price_by_night = column(Integer, default=0, nullable=False)
    latitude = column(float, nullable=True)
    longitude = column(Integer, default=0, nullable=True)



    

