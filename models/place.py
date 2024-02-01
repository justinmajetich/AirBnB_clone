#!/usr/bin/python3
""" Place Module for HBNB project """
import os

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import models
from models.base_model import Base, BaseModel
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """


    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    user = relationship(
        'User', back_populates='places', cascade='all, delete-orphan', single_parent=True)
    cities = relationship('City', back_populates='places')

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            "Review",
            back_populates="place",
            cascade="all, delete, delete-orphan"
        )
    else:
        @property
        def reviews(self):
            """ Getter for reviews. """
            reviews_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
