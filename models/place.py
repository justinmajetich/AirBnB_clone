#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, VARCHAR, Integer, Float


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(VARCHAR(60), ForeignKey('users.id'), nullable=False)
    user_id = Column(VARCHAR(60), ForeignKey('users.id'), nullable=False)
    name = Column(VARCHAR(128), nullable=False)
    description = Column(VARCHAR(128))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, default=0, nullable=False)
    longitude = Column(Float, default=0, nullable=False)
    amenity_ids = []
