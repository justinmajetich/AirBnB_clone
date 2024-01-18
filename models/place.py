#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Float
from os import getenv

class Place(BaseModel):
    """ A place to stay """
    storageType = getenv("HBNB_TYPE_STORAGE")
    if storageType == "db":
        __tablename__ = "places"
        city_id = Column(ForeignKey(cities.id), String(60), nullable=False)
        user_id = Column(ForeignKey(users.id), String(60), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = ""
        number_bathrooms = ""
        max_guest = ""
        price_by_night = ""
        latitude = ""
        longitude = ""
