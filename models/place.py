#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.review import Review


class Place(BaseModel, Base):
    __tablename__ = 'places'
    """ A place to stay """
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=True, default=0)
    number_bathrooms = Column(Integer, nullable=True, default=0)
    max_guest = Column(Integer, nullable=True, default=0)
    price_by_night = Column(Integer, nullable=True, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    # amenity_ids = []
    reviews = relationship('Review', backref='place', cascade='all, delete')

    @property
    def reviews(self):
        """ getter for reviews """
        review_list = []
        for key, value in models.storage.all(Review).items():
            if value.place_id == self.id:
                review_list.append(value)
        return review_list
