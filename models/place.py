#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
import shlex

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                        Column("place_id", String(60),
                                ForeignKey("places.id"),
                                primary_key=True,
                                nullable=False),
                        Column("amenity_id", String(60),
                                ForeignKey("amenities.id"),
                                primary_key=True,
                                nullable=False))


class Place(BaseModel, Base):
    """This is the class place"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
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
        amenity_ids = []

  
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
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

        def __init__(self, *args, **kwargs):
            """initializes place"""
            super().__init__(*args, **kwargs)

        @property
        def reviews(self):
            """ Returns to list of reviews.id """
            val = models.storage.all()("Review").values()
            list = []
            for obj in val:
                if obj.place_id == self.id:
                    list.append(obj)
            return list
        
    if getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def amenities(self):
            """ Returns to list of amenity.id """
            val = models.storage.all()("Amenity").values()
            list = []
            for obj in val:
                if obj.place_id == self.id:
                    list.append(obj)
            return list
