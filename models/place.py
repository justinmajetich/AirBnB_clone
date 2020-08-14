#!/usr/bin/python3
"""Place Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models
from os import getenv


class Place(BaseModel, Base):
    """A place to stay."""

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

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     nullable=False))

        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='places', viewonly=False)
    else:
        amenity_ids = ""

        @property
        def amenities(self):
            """Amenities getter."""
            if not self.amenity_ids or type(self.amenity_ids) is not tuple:
                return []
            all_amenities = models.storage.all(Amenities)
            amenities = filter(lambda amenity: amenity.id in self.amenity_ids,
                               all_amenities)
            return amenities

        @amenities.setter
        def amenities(self, amenity):
            """Amenities setter of amenity id."""
            if type(amenity) is not Amenity:
                return

            if not self.amenity_ids or type(self.amenity_ids) is not tuple:
                self.amenity_ids = []
            self.amenity_ids.append(amenity.id)