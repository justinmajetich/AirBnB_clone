#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv
from models.amenity import Amenity


if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship("Review", backref="place",
                               cascade='all, delete')
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """getter for list of reviews"""
            new_list = []
            all_reviews = models.storage.all(Review)
            for key in all_reviews:
                if all_reviews[key] == self.id:
                    new_list.append(all_reviews[key])
            return new_list

        @property
        def amenities(self):
            """getter for list of amenities"""
            new_list = []
            all_amenities = models.storage.all(Amenity)
            for key in all_amenities:
                if all_amenities[key] in self.amenity_ids:
                    new_list.append(all_amenities[key])
            return new_list

        @amenities.setter
        def amenities(self, value):
            """adds a new aminity"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
