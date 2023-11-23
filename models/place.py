#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from os import getenv
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table(
            'place_amenity', Base.metadata,
            Column(
                'place_id',
                String(60),
                ForeignKey('places.id'),
                nullable=False,
                primary_key=True
                ),
            Column(
                'ameity_id',
                String(60),
                ForeignKey('amenities.id'),
                nullable=False,
                primary_key=True
            ))


class Place(BaseModel):
    """ A place to stay """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
                'Review',
                cascade="all, delete, delete-orphan",
                backref='place'
                )
        amenities = relationship(
                'Amenities',
                secondary='place_amenity',
                viewonly=False,
                backref="place_amenities")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def review(self):
        """ returns the list of Review instances"""
        reviews_place = []
        for value in storage.all(Review).values():
            if value.place_id == self.id:
                reviews_place.append(value)
        return reviews_place

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """returns the list of Amenity instances """
            amenities_place = []
            for value in storage.all('Amenities').values():
                if value.place_id == self.id:
                    amenities_place.append(value)
            return amenities_place
