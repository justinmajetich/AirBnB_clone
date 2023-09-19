#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """Represents a place for a database.

    Inherits from SQLAlchemy Base and links to the MySQL table places.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store places.
        city_id (sqlalchemy String): The place's city ID.
        user_id (sqlalchemy String): The user ID of the owner.
        name (sqlalchemy String): The name of the place.
        description (sqlalchemy String): The description of the place.
        number_rooms (sqlalchemy Integer): The number of rooms in the place.
        number_bathrooms (sqlalchemy Integer): The number of bathrooms in the place.
        max_guest (sqlalchemy Integer): The maximum number of guests.
        price_by_night (sqlalchemy Integer): The price per night.
        latitude (sqlalchemy Float): The latitude coordinate of the place.
        longitude (sqlalchemy Float): The longitude coordinate of the place.
    """
    __tablename__ = "places"
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

