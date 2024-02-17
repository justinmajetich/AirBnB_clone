#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class Place(BaseModel, Base):
    __tablename__ = "places"
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

    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PlaceAmenity(Base):
    __tablename__ = "place_amenity"
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False,
                      primary_key=True)
    amenity_id = Column(String(60), ForeignKey('amenities.id'), nullable=False,
                        primary_key=True)