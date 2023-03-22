#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

Base = declarative_base()


class Place(BaseModel, Base):
    """ The Place Class that hosts several class attributes """
    __tablename__ = 'places'
    user = relationship('User', back_populates='places')
    cities = relationship('City', back_populates='places')
    reviews = relationship('Review', back_populates='places',
                           cascade='all, delete')

    city_id = Column(String(60), ForeignKey(cities.id), nullable=False)
    user_id = Column(String(60), ForeignKey(users.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    @property
    def reviews(self):
        """Getter attribute that returns a list of Review instances"""
        review_list = []
        for review in self.review_list:
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
