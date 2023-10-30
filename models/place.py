#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.sql.schema import ForeignKey
from models import storage
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []


amenities = relationship("Place", secondary="Amenity", viewport=False)


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', Integer, ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', Integer, ForeignKey('amenities.id'), primary_key=True)
)


@property
def amenities(self):
    return [
        amenity_id
        for amenity_id in self.amenity_ids
        if amenity_id in Amenity.amenities
    ]


@amenities.setter
def amenities(self, amenity):
    if isinstance(amenities, Amenity):
        self.amenity_ids.append(amenity.id)
