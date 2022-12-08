#!/usr/bin/python3
""" Place Module for HBNB project """
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float, Interger


class Place(BaseModel):
    """ A place to stay
    Args:
        __tablename__ (str): name of table in database
        city_id (str): city where is the place
        user_id (str): user of the place
        name (str) = name of the place
        description (str): descrition of the place
        number_rooms (Integer): number of rooms
        number_bathrooms (Integer): number of bathrooms
        max_guest (Integer): number of guest
        price_by_night (Integer): price of the place
        latitude (Float): latitude
        longitude (Float): longitude
        amenity_ids = []
    """
    __tablename__ = 'places'
    city_id = Column(String(128), nullable=False,
                     ForeignKey('cities.id', ondelete='CASCADE'))
    user_id = Column(String(128), nullable=False,
                     ForeignKey('users.id', ondelete='CASCADE'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
