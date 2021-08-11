#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenities import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade="all")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)

    else:
        from models import storage
        from models.reviews import Review

        @property
        def reviews(self):
            """ Returns the list of Review instances with
                place_id equals to the current Place.id
            """
            reviews = []
            for place in storage.all(Review).values():
                if place.id == self.place_id:
                    reviews.append(place)
            return reviews

        @property
        def amenities(self):
            """ Returns the list of Amenity instances based on the attribute
                amenity_ids that contains all Amenity.id linked to the Place.
            """
            amenities = []
            for amenity in storage.all(Amenity).values():
                if amenity.id == self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, obj):
            """ Handles append method for adding an
                Amenity.id to the attribute amenity_ids.
            """
            if type(obj).__name__ == "Amenity":
                self.amenity_ids.append(obj)
