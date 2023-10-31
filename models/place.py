#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import Base
import models
from os import getenv

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True,
           nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    __tablename__ = 'places'

    id = Column(String(60), primary_key=True, nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    # Establish relationships

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 back_populates="places", viewonly=False)

    @property
    def amenities(self):
        return [amenity for amenity in self.storage.all(self.amenity).values()
                if amenity.id in self.amenity_id]

    @amenities.setter
    def amenities(self, amenity_obj):
        if isinstance(amenity_obj, self.amenity):
            self.amenity_ids.append(amenity_obj.id)
