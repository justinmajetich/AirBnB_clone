#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table

place_amenity = Table(
    "place_amenity", Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete"
        )
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False,
            back_populates="place_amenities"
        )
    else:
        @property
        def reviews(self):
            """returns list of Review instances upon place_id"""
            reviews_list = []
            for obj in models.storage.all('Review').values():
                if obj.place_id == self.id:
                    reviews_list.append(obj)
            return reviews_list

        @property
        def amenities(self):
            """returns list of Amenity instances upon place_id"""
            amenities_list = []
            for amenity in models.storage.all('Amenity').values():
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, value):
            """setter for amenity_ids list - class attribute"""
            if type(value) is Amenity and value.id not in self.amenity_ids:
                self.amenity_ids.append(value.id)
