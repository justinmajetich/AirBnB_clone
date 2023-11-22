#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Foreignkey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from os import getenv

place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
        )

class Place(BaseModel, Base):
    """ A place to stay
    Attributes:
        city_id = city id
        user_id = user id
        name = name input
        description = description string
        number_rooms = Integer num of rooms
        number_bathrooms = integer number of bathrooms
        max_guest = number of maximum guest in integer
        price_by_night = price in integer
        latitude = latitude in float
        longitude = longitude in float
        amenity_ids = List of amenities id
    """

    __tablename__ == "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), foreignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    number_rooms = Column(Intger, nullable=False, default=0)
    max_guest = Column(integer, nullable+false, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)

    user = relationship('User', back_populates='places')
    city = relationship('City', back_populate='places')
    amenities = relationship('Amenity', secondary=place_amenity, back_populate='place_amenities')
    reviews = relationship('Review', back_populates='place', cascade='all delete')

    if getenv("HBNB_TYPE_STORAGE") =="db":
        review = relationship("Review", cascade='all, dlete, delte-orphan',
                backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                viewonly=False, vack_populates="place_amenities")

    else:
        @amenities.setter
        def amenities(self, obj=None):
            """Appends method for adding amenity id attribute"""
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)

        def amenities(self):
            """Return list of amenity instance"""
            return self.amenity_ids
