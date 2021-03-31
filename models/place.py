#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    city_id = "Column(String(60), nullable=False, ForeignKey('cities.id'))"
    user_id = "Column(String(60), nullable=False, ForeignKey('user.id'))"
    name = "Column(String(128), nullable=False)"
    description = "Column(String(1024), nullable=True)"
    number_rooms = "Column(Int, default=0, nullable=False)"
    number_bathrooms = "Column(Int, default=0, nullable=False)"
    max_guest = "Column(Int, default=0, nullable=False)"
    price_by_night = "Column(Int, default=0, nullable=False)"
    latitude = "Column(Float, nullable=True)"
    longitude = "Column(Float, nullable=True)"
    amenity_ids = []
    __tablename__ = 'places'
