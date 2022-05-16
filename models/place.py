#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
import os

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="user", cascade="delete")
    place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
    )
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        """Return a list with the citites"""
        review_dict = models.storage.all(Review)
        review_list = []
        for key, value in review_dict.items():
            if value.place_id == self.id:
                review_list.append(value)
        return review_list

    @property
    def amenities(self):
        """Return a list with the citites"""
        from models.amenity import Amenity
        amenity_dict = models.storage.all(Amenity)
        amenities_list = []
        for key, value in amenity_dict.items():
            if value.id in self.amenity_ids:
                amenities_list.append(value)
        return amenities_list

    @amenities.setter
    def amenities(self, amenity):
        """Setter for amenity_ids"""
        from models.amenity import Amenity
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
