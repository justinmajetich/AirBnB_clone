#!/usr/bin/python3
"""This is the place class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import shlex
import models


class Place(BaseModel, Base):
    """This is a class for place"""

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

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

    else:
        @property
        def reviews(self):
            """
            getter attribute reviews that returns the list of Review instances
            with place_id equals to the current Place.id
            """
            var = models.storage.all()
            all_reviews = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if review[0] == 'Review':
                    all_reviews.append(var[key])
                for elements in all_reviews:
                    if elements.place_id == self.id:
                        result.append(elements)
            return result
