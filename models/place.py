#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import String, Float, Integer, ForeignKey, Column, Table
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import relationship
from sqlalchemy.schema import MetaData
import os
from models import storage

metadata = Base.metadata

place_amenity = Table(
    'place_amenity',
    metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place', cascade="delete")
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False)
    else:
        @property
        def reviews(self):
            """ Method that gets reviews"""
            reviewList = []
            for review in storage.all(Review).values():
                if review.getattr('place_id') == self.id:
                    reviewList.append(review)
            return(reviewList)

        @property
        def amenities(self):
            """ Method that gets amenities"""
            ''' for row in place_amenity: row.place_id and amenity.id
                 == row.amenity_id:'''
            amenList = []
            for amenity in storage.all(Amenity).value():
                if self.id == amenity.place_id:
                    amenList.append(amenity)
            return(amenList)

        @amenities.setter
        def amenities(self, obj):
            """ Method to set amenities """

            if isinstance(obj, Amenity):
                self.append(obj)
