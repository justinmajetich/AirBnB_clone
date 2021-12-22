#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship, relationships
from os import getenv
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """

    env = getenv('HBNB_TYPE_STORAGE')

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if env == 'db':
        reviews = relationship('Review', backref="places")
    else:
        @property
        def reviews(self):
            review_dict = models.storage.all(Review)
            review_list = []
            for key, value in review_dict.items():
                if value.place_id == self.id:
                    review_list.append(value)
            return review_list
