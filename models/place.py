#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from os import getenv

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    if 'db' == getenv('HBNB_TYPE_STORAGE=db'):
        city_id = Column(String(60), nullable=False, ForeignKey='cities.id')
        user_id = Column(String(60), nullable=False, ForeignKey='users.id')
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latittude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

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
