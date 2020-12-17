#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Table
from models.review import Review
import models

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column(
        'place_id', String(60), ForeignKey("places.id"),
        primary_key=True, nullable=False),
    Column(
        'amenity_id', String(60), ForeignKey("amenities.id"),
        primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship(
        "Review", backref="place", cascade="all, delete-orphan")

    amenities = relationship(
        "Amenity", secondary=place_amenity, viewonly=False)

    if getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def reviews(self):
            """ Get a list of all related Review current Place"""
            reviews = models.storage.all(Review)
            l_revw = []
            for review in reviews.items():
                if review.place_id == self.id:
                    l_revw.append(review)
            return l_revw

        @property
        def amenities(self):
            """that returns the list of Amenity instances based on the
            attribute amenity_ids that contains all Amenity.id linked to the
            Place"""
            from models.amenity import Amenity
            amenities = models.storage.all(Amenity)
            l_Ame = []
            for classId, amenity in amenities.items():
                if amenity.place_id == self.id:
                    l_Ame.append(amenity)
            return l_Ame

        @amenities.setter
        def amenities(self, value):
            """handles append method for adding an Amenity.id to the attribute
            amenity_ids"""
            from models.amenity import Amenity
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
