#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy,orm import relationship
from sqlalchemy import Table

place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
            primary_key=True, nullable=False)
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
            primary_key=True, nullable=False)
        )


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

    reviews = relationship('Review', cascade='delete, delete-orphan',
                           backref='place')
    amenities = relationship('Amenity', secondary='place_amenity',
                             viewonly=False)
    storage_type = os.getenv('HBNB_TYPE_STORAGE')
    if storage_type != 'db':
        @property
        def amenities(self):
            """Returns the list of Amenity Instances base on the attribute
            amenity_ids that contains all Amenity.id linked to the Place"""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)

        @property
        def reviews(self):
            """Returns the list of Review instances with
            place_id equals to the current Place.id"""
            review_objects = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_objects.append(review)
            return review_objects
