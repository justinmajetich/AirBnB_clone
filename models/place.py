#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    storageType = getenv("HBNB_TYPE_STORAGE")
    if storageType == "db":
        reviews = relationship('Review', cascade="all, delete, delete-orphan",
                          backref='place')
    else:
        @property
        def reviews(self):
            """ getter for reviews in filestorage use"""
            from models import storage
            reviewList = []
            
            for val in storage.all(Review).values():
                if val.place_id == self.id:
                    reviewList.append(val)
            return reviewList
        
