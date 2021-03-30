#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from models.city import City
from os import getenv


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("user.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False)
    number_bathrooms = Column(Integer, nullable=False)
    max_guest = Column(Integer, nullable=False)
    price_by_night = Column(Integer, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
