#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from models.city import cities
from models.user import users


class Place(BaseModel):
    """ A place to stay """
    __tablename__= 'places'
    city_id = Column(String(60), ForeignKey(cities.id), nullable=False)
    user_id = Column(String(60), ForeignKey(users.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, default=0)
    longitude = Column(Float, default=0)
    amenity_ids = []
