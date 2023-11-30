#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


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
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Getter attribute reviews that returns the list of Review instances"""
            review_list = []
            all_reviews = models.storage.all(Review)
            for revs in all_reviews.values():
                if revs.place_id == self.id:
                    review_list.append(revs)
            return review_list

        @property
        def amenities(self):
            """Getter attribute amenities that returns the list of Amenity instances"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute amenities that handles append method for adding an Amenity.id
            to the attribute amenity_ids"""
            if type(obj).__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
