#!/usr/bin/python3
""" Place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import os
from models.review import Review
from models.amenity import Amenity
import models


place_amenity = Table('place_amenity',Base.metadata,
                          column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))
                                

class Place(BaseModel):
    """ 
    A place to stay 
    """
    
    city_id = column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = column(String(60), ForeignKey('user_id'), nullable=False)
    name = column(String(128), nullable=False)
    description = column(String(1024), nullable=True)
    number_rooms = column(Integer, default=0, nullable=False)
    number_bathrooms = column(Integer, default=0, nullable=False)
    max_guest = column(Integer, default=0, nullable=False)
    price_by_night = column(Integer, default=0, nullable=False)
    latitude = column(float)
    longitude = column(Integer)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals
            to the current Place.id."""

            reviews = list(models.storage.all(Review).values())

            return list(
                filter(lambda review: (review.place_id == self.id), reviews))

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on
            the attribute amenity_ids that contains all Amenity.id."""

            amenities = list(models.storage.all(Amenity).values())

            return list(
                filter(lambda amenity: (amenity.place_id in self.amenity_ids),
                       amenities))

        @amenities.setter
        def amenities(self, value=None):
            """Adds ids in amenity_ids ."""
            if type(value) == type(Amenity):
                self.amenity_ids.append(value.id)
    
   
  




    

