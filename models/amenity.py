#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', Integer, ForeignKey('places.id')),
                      Column('amenity_id', Integer, ForeignKey('amenities.id'))
                      )


class Place(BaseModel, Base):
    """The class Place and its attributes"""
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

    # Relationship with Amenity via place_amenity table
    amenities = relationship("Amenity", secondary=place_amenity,
                             back_populates="places")


class Amenity(BaseModel, Base):
    """Amenity class with attributes"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    # Relationship with Place via place_amenity table
    places = relationship("Place", secondary=place_amenity,
                          back_populates="amenities")
