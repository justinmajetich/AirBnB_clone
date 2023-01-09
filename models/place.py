#!/usr/bin/python3
""" Place Module for HBNB project """

from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship
from os import environ
import models

place_amenity = Table("place_amenity", Base.metadata,
        Column("place_id", String(60), 
            ForeignKey("places.id"), 
            primary_key=True, nullable=False),
        Column("amenity_id", String(60),
            ForeignKey("amenities.id"),
            primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """
        Place class to represent places
        Place class to represent places
    """
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
    amenity_ids = []

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        reviews = relationship("Review", back_populates="place")
        amenities = relationship("Amenity",
                                secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """ getter returns list of reviews """
            list_of_reviews = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    list_of_reviews.append(review)
            return list_of_reviews

        @property
        def amenities(self):
            """ getter returns list of amenities """
            list_of_amenities = []
            all_amenities = models.storage.all(Amenity)
            for key, obj in all_amenities.items():
                if key in self.amentiy_ids:
                    list_of_amenities.append(obj)
            return list_of_amenities

        @amenities.setter
        def amenities(self, obj=None):
            """Set amenity_ids
            """
            if type(obj).__name__ == 'Amenity':
                new_amenity = 'Amenity' + '.' + obj.id
                self.amenity_ids.append(new_amenity)