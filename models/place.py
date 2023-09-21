#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """
        This is the place model
        Inherits:
            Base
            BaseModel
        Attributes:
            __tablename__: the database table name
            city_id: the city id foreign key
            user_id: the user id foreign key
            name: place name column
            description: place description
            number_rooms: number of rooms in the place
            max_guest: guest the room can allow
            number_bathrooms: bathrooms in the place
            price_by_night: situation at night
            latitude: latitude point on the map
            longitude = longitude point on the map
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
