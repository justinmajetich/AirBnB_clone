#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import String, Column, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


amenity_table = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey("amenities.id"),
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

    reviews = relationship("Review", cascade="delete", backref="place")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

if getenv("HBNB_TYPE_STORAGE") != "db":
    @property
    def reviews(self):
        """getter for reviews for FileStorage"""
        r_list =[]
        for review in list(models.storage.all(Review).values()):
            r_list.append(review)
        return r_list

    @property
    def amenities(self):
        """getter for amenities for FileStorage"""
        a_list = []
        for amenity in list(models.storage.all(Amenity).values()):
            a_list.append(amenity)
        return a_list

    @amenities.setter
    def amenities(self, obj):
        """setter for amenities for FileStorage"""
        if type(obj) == Amenity:
            self.amenity_ids.append(obj.id)
