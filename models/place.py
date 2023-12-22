#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table, ForeignKey
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id',),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if storage_type == 'db':
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
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref='places_amenities', viewonly=False,)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_bathrooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter attribute reviews that
            returns the list of Review instances
            with place_id equals to the current Place.id"""
            from models import storage
            from models.review import Review
            reviews = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """getter attribute amenities that returns the list of Amenity
            instances based on the attribute amenity_ids that contains all
            Amenity.id linked to the Place"""
            from models import storage
            from models.amenity import Amenity
            amenities = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, obj):
            """setter attribute amenities that handles append method for adding"""
            from models.amenity import Amenity
            if type(obj) == type(Amenity):
                self.amenity_ids.append(obj.id)
