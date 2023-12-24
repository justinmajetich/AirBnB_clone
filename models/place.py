#!/usr/bin/python3
"""
    module containing places to represent the place
    module containing places to represent the place
"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")

if storage_engine == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """
        Place class to represent places
        Place class to represent places
    """
    __tablename__ = "places"
    if (storage_engine == "db"):
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
        reviews = relationship("Review", back_populates="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 back_populates="place_amenities",
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
            """getter function for reviews attribute"""
            result = []
            temp = models.dummy_classes['Review']
            for r in models.storage.all(temp).values():
                if r.place_id == self.id:
                    result.append(r)
            return result

        @property
        def amenities(self):
            """getter function for amenity attribute"""
            result = []
            temp = models.dummy_classes['Amenity']
            for a in models.storage.all(temp).values():
                if a in self.amenity_ids:
                    result.append(a)
            return result

        @amenities.setter
        def amenities(self, obj):
            """ setter for amenities class """
            temp = models.dummy_classes['Amenity']
            if (isinstance(obj, models.storage.all(temp))):
                self.amenity_ids.append(obj.id)
