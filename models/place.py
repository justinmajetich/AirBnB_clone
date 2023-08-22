#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import ForeignKey 
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """ A place to stay for storing place information"""

    __tablename__ = 'places'

    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False,  default value=0)
    number_bathrooms = Column(Integer, nullable=False, default value=0)
    max_guest = Column(Integer, nullable=False, default value=0)
    price_by_night = Column(Integer, nullable=False, default value=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
