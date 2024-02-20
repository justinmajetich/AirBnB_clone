#!/usr/bin/python3
""" Place Module for HBNB project """

from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv

class Place(BaseModel, Base):

    __tablename__ = "places"

    # if getenv('HBNB_TYPE_STORAGE') == 'db':
    #     place_amenity = Table('place_amenity', Base.metadata,
    #                           Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    #                           Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

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
    # reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
    # amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    # users = relationship("User", backref="places")
    # cities = relationship("City", backref="places")

    # else:
    #     city_id = ""
    #     user_id = ""
    #     name = ""
    #     description = ""
    #     number_rooms = 0
    #     number_bathrooms = 0
    #     max_guest = 0
    #     price_by_night = 0
    #     latitude = 0.0
    #     longitude = 0.0
    #     amenities = []
    #     reviews = []

    # def __init__(self, *args, **kwargs):
    #     """initializes Place"""
    #     super().__init__(*args, **kwargs)