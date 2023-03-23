#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

from os import getenv

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        nullable=False,
        primary_key=True
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        nullable=False,
        primary_key=True
    )
)
"""Represents the many to many relationship table
between Place and Amenity records.
"""


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(
        String(60),
        ForeignKey('cities.id'),
        nullable=False,
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(
        String(60),
        ForeignKey('users.id'),
        nullable=False,
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    name = Column(
        String(128),
        nullable=False,
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    description = Column(
        String(1024),
        nullable=False,
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    number_rooms = Column(
        Integer,
        default=0,
        nullable=False,
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    number_bathrooms = Column(
        Integer,
        default=0,
        nullable=False,
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    max_guest = Column(
        Integer,
        default=0,
        nullable=False,
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    price_by_night = Column(
        Integer,
        default=0,
        nullable=False,
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    latitude = Column(
        Float,
        default=0.0,
        nullable=False,
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    longitude = Column(
        Float,
        default=0.0,
        nullable=False,
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    amenity_ids = []
    reviews = relationship(
        'Review',
        cascade='all, delete, delete-orphan',
        backref='places'
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else None
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship(
            'Amenity',
            secondary='place_amenity',
            viewonly=False,
            backref='place_amenities'
        )
    else:
        @property
        def amenities(self):
            """ Getter for amenities of a place """
            from models import storage
            from models.amenity import Amenity
            amenities = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, obj):
            """ Setter for amenities of a place """
            if obj.__class__.__name__ == 'Amenity':
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)

        @property
        def reviews(self):
            """ Getter for reviews of a place"""
            from models import storage
            from models.review import Review
            reviews = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews
