#!/usr/bin/python3
""" Place Module for HBNB project """
from ast import For, In, Str
from re import I
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from models import storage
from models.amenity import Amenity
from models.review import Review
from os import getenv


Table('place_amenity', Base.metadata,
      Column('place_id', ForeignKey('places.id'), nullable=False,
             primary_key=True),
      Column('amenity_id', ForeignKey('amenities.id'),
             nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete-orphan')

        amenities = relationship(
            'Amenity',
            secondary='place_amenity',
            backref='place_amenities',
            viewonly=False)
    else:
        @property
        def reviews(self):
            """ getter for reviews """
            rev_list = []
            for review in storage.all(Review).values():
                if review.getattr('place_id') == self.id:
                    rev_list.append(review)
            return rev_list

        @property
        def amenities(self):
            """getter for amenities"""
            amn_list = []
            for amenity in storage.all(Amenity).value():
                if self.id == amenity.place_id:
                    amn_list.append(amenity)
            return amn_list

        @amenities.setter
        def amenities(self, obj):
            """setter for amenities"""
            if isinstance(obj, Amenity):
                self.append(obj)
