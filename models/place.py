#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb
import shlex
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if models.storage.__class__ is DBStorage:
        reviews = relationship("Review", cascade='all,
                               delete, delete-orphan', ref='place')

    elif models.storage.__class__ is FileStorage:
        @property
        def reviews(self):
            """ this is a getter function for review objects """

            rev = []

            for k, v in models.storage.all(Review).items():
                if v.place_id == self.id:
                    rev.append(v)
            return rev
