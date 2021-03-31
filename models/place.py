#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import Table, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from os import getenv


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"), primary_key=True,
                             nullable=False))


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
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False, backref="Places")
    else:
        @property
        def reviews(self):
            """ Lists Of Instances Of Reviews """
            reviewsList = []
            allReviews = models.storage.all(Review)
            for review in allReviews.values():
                if review.place_id == self.id:
                    reviewsList.append(review)
            return reviewsList

        @property
        def amenities(self):
            """ List of Instances of Amenity """
            amenitiesList = []
            allAmenities = models.storage.all(Amenity)
            for amenity in allAmenities.values():
                if amenity.id in self.amenity_ids:
                    amenitiesList.append(amenity)
                return amenitiesList

        @amenities.setter
        def amenities(self, value):
            """ Method for adding an Amenity.id to attribute amenity_ids"""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
