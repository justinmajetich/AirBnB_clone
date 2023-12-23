#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
from models.base_model import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey, Float, Table
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer(), default=0, nullable=False)
    number_bathrooms = Column(Integer(), default=0, nullable=False)
    max_guest = Column(Integer(), default=0, nullable=False)
    price_by_night = Column(Integer(), default=0, nullable=False)
    latitude = Column(Float(), nullable=False)
    longitude = Column(Float(), nullable=False)

    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                                 Column('amenity_id', String(60),
                                        ForeignKey('amenities.id'),
                                     primary_key=True, nullable=False))
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
