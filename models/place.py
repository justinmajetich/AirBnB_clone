#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey


class Place(BaseModel):
    """ Represents a Place for a MySQL database

    Attributes:
    __tablename__ (str): The name of the MySQL table to store places
    city_id (sqlalchemy String): The place's City id
    user_id (sqlalchemy String): The place's user id
    name (sqlalchemy String): The place's City name 
    description (sqlalchemy String): The place's description
    number_rooms (sqlachemy Integer): The place's number of rooms
    number_bathrooms (sqlachemy Integer): The place's number of bathrooms
    max_guest (sqlachemy Integer): The place's number of guests
    price_by_night (sqlachemy Integer): The price by night
    latitude (sqlalchemy Float): The place's latitude
    longitude (sqlalchemy Float): The place's longitude
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
