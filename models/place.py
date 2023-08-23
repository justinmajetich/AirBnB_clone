#!/usr/bin/python3
"""
Place Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Place(BaseModel, Base):
    """ A place to stay """
    
    __tablename__ = "places"
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
