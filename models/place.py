#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="place_amenities",
                                 viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Returns list of reviews """
            reviews = models.storage.all(Review)
            lst = []
            for review in reviews.values():
                if review.place_id == self.id:
                    lst.append(review)
            return lst

        @property
        def amenities(self):
            """Amenities getter"""
            amenities = models.storage.all(Amenity)
            lst = []
            for amenity in amenities.values():
                if amenity.id in self.amenity_ids:
                    lst.append(amenity)
            return lst

        @amenities.setter
        def amenities(self, obj):
            """Amenities setter"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
