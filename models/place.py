#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
               primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
               primary_key=True, nullable=False)
    )


class Place(BaseModel, Base):
    """ Class that defines a place"""

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer(), nullable=False,  default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0)
    price_by_night = Column(Integer(), nullable=False, default=0)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review",
                               backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 backref="place_amenities",
                                 viewonly=False)
    else:  # if file storage
        @property
        def reviews(self):
            """Getter for reviews of this place saved in FileStorage"""
            reviews = []
            for review in models.storage.all(Review).values():
                # grab only review associated with this place
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """Getter for amenities of this place saved in FileStorage"""
            amenities = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.place_id == self.id:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, object):
            """ Setter for amenities """
            if type(object) is Amenity:
                self.amenity_ids.append(object.id)
