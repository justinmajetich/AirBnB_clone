#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import models
from models.review import Review


place_amenity = Table("place_amenity", Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")
    amenities = relationship("Amenity", secondary="place_amenity",
                             backref="place_amenities", viewonly=False)

    @property
    def reviews(self):
        """review getter. yelp for dorks"""
        yelp = []
        for x in models.storage.all(Review):
            if getattr(x, "Place.id") == self.id:
                yelp.append(x)
        return(yelp)

    @property
    def amenities(self):
        return self.amenity_ids

    @amenities.setter
    def amenities(self, amenity):
        self.amenity_ids.append(amenity)
