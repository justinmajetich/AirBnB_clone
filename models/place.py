#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
import models
from os import getenv

place_amenity_table = Table('place_amenity', Base.metadata,
                            Column('place_id', String(60),
                                   ForeignKey('places.id'),
                                   primary_key=True, nullable=False),
                            Column('amenity_id', String(60),
                                   ForeignKey('amenities.id'),
                                   primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ Made comments just because of testing """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    """ reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False) """

    amenity_ids = []

    # Establish relationships

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """ Added comments just for testing """
            amenity_list = []

            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """ Added setter function """
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
