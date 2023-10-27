#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import relationship


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ The Place for the database

    Inherits from SQLAlchemy Base and links to places table.

    Attributes:
        __tablename__ (str): The name of the table to use.
        city_id (sqlalchemy String): The place's city id.
        user_id (sqlalchemy String): The place's user id.
        name (sqlalchemy String): The name of the place.
        description (sqlalchemy String): The description.
        number_rooms (sqlalchemy Integer): Number of rooms.
        number_bathrooms (sqlalchemy Integer): Number of Bathrooms.
        max_guest (sqlalchemy Integer): Maximum number of guests.
        price_by_night (sqlalchemy Integer): Price by night.
        latitude (sqlalchemy Float): The latitude of the place.
        longitude (sqlalchemy Float): The longitude of the place.
        reviews (sqlalchemy relationship): The Place-Review relation.
        amenities (sqlalchemy relationship): The Place-Amenity relation.
        amenitiy_ids (list): An id list of all linked amenities.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"),
                     nullablle=False)
    user_id = Column(String(60), ForeignKey("users.id"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """ Get a list of the linked Reviews."""
            r_list = []
            for review in list(models.storage.all('Review').values()):
                if review.place_id == self.id:
                    r_list.append(review)
            return r_list

        @property
        def amenities(self):
            """ get or set linked Amenities."""
            a_list = []
            for amenity in list(models.storage.all('Amenity').values()):
                if amenity.id in self.amenity_ids:
                    a_list.append(amenity)
            return a_list

        @amenities.setter
        def amenities(self, value):
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
