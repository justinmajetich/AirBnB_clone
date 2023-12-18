#!/usr/bin/python3

""" Place Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Float, Table
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if storage_type == "db":
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
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
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
        def amenities(self):
            """amenities getter"""
            from models import storage
            Amenity = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    Amenity.append(amenity)
            return Amenity

        @amenities.setter
        def amenities(self, obj):
            """amenities setter"""
            if type(obj).__name__ == "Amenity":
                self.amenity_ids.append(obj.id)


        @property
        def reviews(self):
            """reviews getter"""
            from models import storage
            Review = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    Review.append(review)
            return Review
