#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import String, ForeignKey, Column, Integer, Float
from os import getenv


class Place(BaseModel, Base):
    """
    The Place Class Object, inherits from BaseModel and Base

    attributes:

        city_id (string): foreign key from cities id
        user_id (string): foreign key from states id
        name (string): the name of the place
        description (string): the description of the place
        number_rooms (int): the number of rooms in the place
        number_bathrooms (int): the number of bathroom in place
        max_guest (int): the maximum number of guest in place
        price_by_night (int): the price of place for night
        latitude (float): the latitude of the place
        longitude (float): the longitude of the place
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', backref='places',
                               cascade="all, delete-orphan")
    else:
        @property
        def reviews(self):
            return [obj for obj
                    in FileStorage.all(Review).values()
                    if obj.place_id == self.id]
