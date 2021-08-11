#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.review import Review
import models
from os import getenv
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import Float, Integer
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     primary_key=True),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True))
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
        amenity_ids = []
        reviews = relationship("Review",
                               cascade="all, delete", backref="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity, viewonly=False)

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
            """getter atribute reviews"""
            allReviews = models.storage.all(Review)
            placeReviews = []

            for objReview in list(allReviews.values()):
                if objReview.place_id == self.id:
                    placeReviews.append(objReview)

            return (placeReviews)

        @property
        def amenities(self):
            """getter atribute amenities"""
            allAmenities = models.storage.all(Amenity)
            placeAmenities = []

            for objAmenity in allAmenities.values():
                if objAmenity.id in self.amenity_ids:
                    placeAmenities.append(objAmenity)

            return (placeAmenities)

        @amenities.setter
        def amenities(self, prmObj):
            """amenities setter"""
            if isinstance(prmObj, Amenity):
                self.amenity_ids.append(prmObj.id)
