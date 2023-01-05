#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import MetaData, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    # define schema: name and properties/fields
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
    reviews = relationship("Review", backref="place",
                           cascade="all, delete, delete-orphan")

    amenity_ids = []

    @property
    def reviews(self):
        """ getter attribute that returns the list of Review instances
        with place_id = current Place.id (self.id). This' the FileStorage
        relationship between Place and Review """
        # get all reviews and filter by self.id
        reviews = self.all(Review)
        my_reviews = {}
        for key in reviews.keys():
            if key.partion('.')[2].strip() == self.id:
                my_reviews[key] = reviews[key]
        return my_reviews
