#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class Place(BaseModel, Base):
    """ A place to stay """
    city_id = Column(str(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(str(60), ForeignKey('users.id'), nullable=False)
    name = Column(str(128), nullable=False)
    description = Column(str(1024), nullable=True)
    number_rooms = Column(int, nullable=False, default='0')
    number_bathrooms = Column(int, nulllable=False, default='0')
    max_guest = Column(int, nullable=False, default='0')
    price_by_night = Column(int, nullable=False, default='0')
    latitude = Column(float, nullable=True)
    longitude = Column(float, nullable=True)
    amenity_ids = []
    __tablename__ = 'places'
