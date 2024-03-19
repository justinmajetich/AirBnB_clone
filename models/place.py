#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Table, MetaData, Float
from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.ext.declarative import declarative_base
import models

metadata = Base.metadata


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    place_amenity = Table('place_amenity', metadata,
            Column('place_id', String(60),
                ForeignKey('place.id'),
                primary_key=True,nullable=False)),

            Column('amenity_id', String(60),
                    ForeignKey('amenities.id'),
                    primary_key=True, nullable=False))

            if getenv("HBNB_TYPE_STORAGE") == "db":
                reviews = relationship(
                        "Review", backref="place", cascade="all, delete"
                        )
                amenities = relationship(
                        "Amenity", secondary="place_amenity",viewonly=False
                        )
    else:

        @property
        def reviews(self):
            """Returns a list of review instances"""

            review_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        """ setting the getter """
        def amenities(self):
            """ Returns the list of Amenity instances"""

            amenities_list = []
            for amenity in models.storage.all(amenity_id).values():
                if amenity.place_id == self.id:
                    amenities_list.append(amenity)
            return amenities_list
